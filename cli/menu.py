# ------------------------------------------------------------------------------
# Função: exibir_menu
# Interface de linha de comando para uso contínuo do sistema.
# ------------------------------------------------------------------------------
import os
from core.search import buscar_nos_pdfs
from utils.logger import registrar_log, ARQUIVO_LOG
from utils.highlight import destacar_termo
from utils.terminal import limpar_terminal


def exibir_resultados(resultados: list[dict], termo: str) -> None:
    """
    Exibe os resultados encontrados no terminal.
    Args:
        resultados (list[dict]): Lista de dicionários com as ocorrências encontradas.    
    """
    if not resultados:
        print("\nNenhum resultado encontrado.")
        return

    print(f"\n🔎 {len(resultados)} ocorrência(s) encontradas:\n")
    for r in resultados:
        contexto = destacar_termo(r["contexto"], termo)
        print(f"📘 {r['arquivo']} (pág. {r['pagina']}): ...{contexto}...\n")


def exibir_menu(total_pdfs) -> None:
    """
    Exibe o menu principal do sistema.
    """
    while True:
        print("\n=== Sistema de Busca em PDFs ===")
        print("1. Realizar nova busca")
        print("2. Exibir último log")
        print("3. Limpar logs")
        print("4. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            if total_pdfs == 0:
                print("\n❌ A busca está indisponível.")
                print("➡️  Nenhum arquivo PDF foi encontrado na pasta 'pdfs/'.")
                print("➡️  Copie os arquivos PDF e reinicie o aplicativo.\n")
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
