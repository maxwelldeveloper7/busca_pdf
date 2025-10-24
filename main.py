"""
================================================================================
Aplicativo de Busca em Múltiplos Arquivos PDF
Autor: Maxwell de Oliveira Chaves
Versão: 1.0
Descrição:
    Este aplicativo realiza buscas textuais em todos os arquivos PDF
    contidos em uma pasta local, exibindo e registrando as ocorrências
    encontradas. O sistema foi desenvolvido em Python com foco em uso
    pedagógico, pesquisa de conteúdos e acessibilidade para avaliações
    educacionais online.

Licença: Uso Educacional e Não Comercial.
================================================================================
"""

# Importação de bibliotecas
import os
import pdfplumber
from datetime import datetime

# Definição das pastas do projeto
PASTA_PDFS = "pdfs"
PASTA_RESULTADOS = "resultados"
ARQUIVO_LOG = os.path.join(PASTA_RESULTADOS, "logs_pesquisa.txt")

# ------------------------------------------------------------------------------
# Função: buscar_nos_pdfs
# Percorre todos os arquivos PDF da pasta especificada e busca o termo informado.
# ------------------------------------------------------------------------------
def buscar_nos_pdfs(termo_busca):
    termo_busca = termo_busca.lower()  # Normaliza o termo de busca
    resultados = []

    # Cria a pasta 'resultados' caso não exista
    os.makedirs(PASTA_RESULTADOS, exist_ok=True)

    # Percorre todos os arquivos da pasta pdfs
    for arquivo in os.listdir(PASTA_PDFS):
        if arquivo.endswith(".pdf"):
            caminho_pdf = os.path.join(PASTA_PDFS, arquivo)

            with pdfplumber.open(caminho_pdf) as pdf:
                for i, pagina in enumerate(pdf.pages, start=1):
                    texto = pagina.extract_text() or ""
                    if termo_busca in texto.lower():
                        pos = texto.lower().find(termo_busca)
                        contexto = texto[max(0, pos - 50): pos + len(termo_busca) + 50]
                        resultados.append({
                            "arquivo": arquivo,
                            "pagina": i,
                            "contexto": contexto.strip().replace("\n", " ")
                        })
    return resultados

# ------------------------------------------------------------------------------
# Função: registrar_log
# Salva as ocorrências encontradas em um arquivo de log.
# ------------------------------------------------------------------------------
def registrar_log(termo, resultados):
    os.makedirs(PASTA_RESULTADOS, exist_ok=True)

    with open(ARQUIVO_LOG, "a", encoding="utf-8") as log:
        log.write("\n" + "=" * 80 + "\n")
        log.write(f"Pesquisa realizada em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        log.write(f"Termo pesquisado: {termo}\n")
        log.write(f"Total de ocorrências: {len(resultados)}\n\n")

        for r in resultados:
            log.write(f"Arquivo: {r['arquivo']} | Página: {r['pagina']}\n")
            log.write(f"Contexto: ...{r['contexto']}...\n\n")

# ------------------------------------------------------------------------------
# Função: exibir_resultados
# Mostra no terminal os resultados encontrados.
# ------------------------------------------------------------------------------
def exibir_resultados(resultados):
    if not resultados:
        print("\nNenhum resultado encontrado.")
        return

    print(f"\n🔎 {len(resultados)} ocorrência(s) encontradas:\n")
    for r in resultados:
        print(f"📘 {r['arquivo']} (pág. {r['pagina']}): ...{r['contexto']}...\n")

# ------------------------------------------------------------------------------
# Função: exibir_menu
# Interface de linha de comando para uso contínuo do sistema.
# ------------------------------------------------------------------------------
def exibir_menu():
    while True:
        print("\n=== Sistema de Busca em PDFs ===")
        print("1. Realizar nova busca")
        print("2. Exibir último log")
        print("3. Limpar logs")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            termo = input("\nDigite o termo a ser buscado: ")
            resultados = buscar_nos_pdfs(termo)
            exibir_resultados(resultados)
            registrar_log(termo, resultados)
            print(f"\n🗂️  Log salvo em: {ARQUIVO_LOG}")

        elif opcao == "2":
            if os.path.exists(ARQUIVO_LOG):
                print("\n=== Último Log ===\n")
                with open(ARQUIVO_LOG, "r", encoding="utf-8") as log:
                    conteudo = log.readlines()[-40:]
                    print("".join(conteudo))
            else:
                print("\nNenhum log encontrado.")

        elif opcao == "3":
            if os.path.exists(ARQUIVO_LOG):
                os.remove(ARQUIVO_LOG)
                print("\n📁 Logs removidos com sucesso.")
            else:
                print("\nNenhum log para remover.")

        elif opcao == "4":
            print("\nEncerrando o programa...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

# ------------------------------------------------------------------------------
# Execução principal
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    exibir_menu()
