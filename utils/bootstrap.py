"""Módulo utilitário para inicializar o ambiente de execução."""
from pathlib import Path

PASTA_PDFS = Path("pdfs")
PASTA_RESULTADOS = Path("resultados")


def inicializar_ambiente() -> int:
    """
    Verifica e cria as pastas necessárias para a execução do aplicativo.
    Retorna a quantidade de arquivos PDF encontrados.
    """

    pdfs_criada = False

    if not PASTA_PDFS.exists():
        PASTA_PDFS.mkdir(parents=True, exist_ok=True)
        pdfs_criada = True

    if not PASTA_RESULTADOS.exists():
        PASTA_RESULTADOS.mkdir(parents=True, exist_ok=True)

    arquivos_pdf = list(PASTA_PDFS.glob("*.pdf"))
    total_pdfs = len(arquivos_pdf)

    if pdfs_criada:
        print("\n📂 Pasta 'pdfs/' criada com sucesso.")
        print("➡️  Copie para esta pasta os arquivos PDF que deseja pesquisar.")
        print("➡️  Os arquivos devem estar no formato .pdf\n")

    if total_pdfs == 0:
        print("⚠️  Nenhum arquivo PDF encontrado na pasta 'pdfs/'.")
        print("➡️  Adicione pelo menos um arquivo PDF para habilitar a busca.\n")
    else:
        print(f"📄 {total_pdfs} arquivo(s) PDF encontrado(s) na pasta 'pdfs/'.\n")

    return total_pdfs
