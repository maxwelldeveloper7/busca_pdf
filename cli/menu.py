import os
from core.observer import Observer
from core.ambiente import AmbienteObservable
from core.search import buscar_nos_pdfs
from utils.logger import registrar_log, ARQUIVO_LOG
from utils.highlight import destacar_termo
from utils.terminal import limpar_terminal


class MenuCLI(Observer):
    """
    Menu que observa o ambiente.
    """

    def __init__(self, ambiente: AmbienteObservable):
        self.ambiente = ambiente
        self.ambiente.registrar(self)

    def atualizar(self) -> None:
        """
        Chamado quando o ambiente é reavaliado.
        """
        print(self.ambiente.contexto.mensagem())

    def exibir(self) -> None:
        print(self.ambiente.contexto.mensagem())

        while True:
            print("\n=== Sistema de Busca em PDFs ===")
            print("1. Realizar nova busca")
            print("2. Exibir último log")
            print("3. Limpar logs")
            print("4. Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                total_atual = self.ambiente.total_pdfs()
                
                if total_atual != self.ambiente.contexto.estado.pode_buscar():
                    self.ambiente.verificar_pdfs()
                
                if total_atual == 0:
                    print("\n❌ Busca indisponível.")
                    print("➡️  Adicione PDFs e tente novamente.\n")
                    continue

                termo = input("Digite o termo a ser buscado: ")
                limpar_terminal()
                resultados = buscar_nos_pdfs(termo)
                exibir_resultados(resultados, termo)
                registrar_log(termo, resultados)

            elif opcao == "2":
                if os.path.exists(ARQUIVO_LOG):
                    with open(ARQUIVO_LOG, encoding="utf-8") as log:
                        print("".join(log.readlines()[-40:]))
                else:
                    print("Nenhum log encontrado.")

            elif opcao == "3":
                if os.path.exists(ARQUIVO_LOG):
                    os.remove(ARQUIVO_LOG)
                    print("Logs removidos com sucesso.")

            elif opcao == "4":
                break

            else:
                print("Opção inválida.")


def exibir_resultados(resultados: list[dict], termo: str) -> None:
    if not resultados:
        print("\nNenhum resultado encontrado.")
        return

    print(f"\n🔎 {len(resultados)} ocorrência(s) encontradas:\n")
    for r in resultados:
        contexto = destacar_termo(r["contexto"], termo)
        print(f"📘 {r['arquivo']} (pág. {r['pagina']}): ...{contexto}...\n")
