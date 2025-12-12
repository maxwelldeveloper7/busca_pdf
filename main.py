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
from tqdm import tqdm
import os
import pdfplumber
from datetime import datetime

# Definição das pastas do projeto
PASTA_PDFS = "pdfs"
PASTA_RESULTADOS = "resultados"
ARQUIVO_LOG = os.path.join(PASTA_RESULTADOS, "logs_pesquisa.txt")


# Cria as pasta 'resultados' e 'pdfs'caso não existam
os.makedirs(PASTA_RESULTADOS, exist_ok=True)
os.makedirs(PASTA_PDFS, exist_ok=True)

# ------------------------------------------------------------------------------
# Função: buscar_nos_pdfs
# Percorre todos os arquivos PDF da pasta especificada e busca o termo informado.
# ------------------------------------------------------------------------------
def buscar_nos_pdfs(termo_busca: str) -> list[dict]:
    """
    Busca o termo especificado em todos os arquivos PDF na pasta definida.
    Args:
        termo_busca (str): O termo a ser buscado nos PDFs.
    Returns:
        Retorna uma lista de dicionários com as ocorrências encontradas.
    """
    termo_busca = termo_busca.lower()  # Normaliza o termo de busca
    resultados = []

    # Lista de arquivos PDF válidos encontrados
    arquivos_pdf = [
        arq for arq in os.listdir(PASTA_PDFS) if arq.endswith(".pdf")]
    
    # Armazena o total de arquivos encontrados
    total = len(arquivos_pdf)
        


    # Primeiro: contar quantas páginas serão processadas (para a barra de progresso)
    total_paginas = 0
    for arquiv in arquivos_pdf:
        caminho_pdf = os.path.join(PASTA_PDFS, arquiv)
        try:
            with pdfplumber.open(caminho_pdf) as pdf:
                total_paginas += len(pdf.pages)
        except Exception:
            continue # Ignora PDFs corrompidos


    # cria a barra de progresso com o toal de páginas
    with tqdm(total = total_paginas,
            desc=f"Procurando em {total} arquivos pelo termo '{termo_busca}'",
            unit="páginas",
            ncols=100,
            # colour='green',
            bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} {unit}") as barras:
    

        # Segundo: executar a busca
        for arquivo in arquivos_pdf:
            caminho_pdf = os.path.join(PASTA_PDFS, arquivo)
            try:
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
                        barras.update(1)  # Atualiza a barra de progresso
            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo}: {e}")
    return resultados

# ------------------------------------------------------------------------------
# Função: registrar_log
# Salva as ocorrências encontradas em um arquivo de log.
# ------------------------------------------------------------------------------
def registrar_log(termo: str, resultados: list[dict]) -> None:
    """
    Registra as ocorrências encontradas em um arquivo de log.
    Args:
        termo (str): O termo buscado.
        resultados (list[dict]): Lista de dicionários com as ocorrências encontradas.
    """
    if not os.path.exists(PASTA_RESULTADOS):
        os.makedirs(PASTA_RESULTADOS)

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
def exibir_resultados(resultados: list[dict]) -> None:
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
        print(f"📘 {r['arquivo']} (pág. {r['pagina']}): ...{r['contexto']}...\n")

# ------------------------------------------------------------------------------
# Função: exibir_menu
# Interface de linha de comando para uso contínuo do sistema.
# ------------------------------------------------------------------------------
def exibir_menu():
    """
    Exibe o menu principal do sistema.
    """    
    while True:
        print("\n=== Sistema de Busca em PDFs ===")
        print("1. Realizar nova busca")
        print("2. Exibir último log")
        print("3. Limpar logs")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            termo = input("\nDigite o termo a ser buscado: ")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal
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
