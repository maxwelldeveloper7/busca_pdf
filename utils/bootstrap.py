from pathlib import Path
from core.context import AmbienteContexto
from core.ambiente import AmbienteObservable

PASTA_PDFS = Path("pdfs")
PASTA_RESULTADOS = Path("resultados")


def inicializar_ambiente() -> AmbienteObservable:
    if not PASTA_PDFS.exists():
        PASTA_PDFS.mkdir(parents=True, exist_ok=True)
        print("\n📂 Pasta 'pdfs/' criada com sucesso.")
        print("➡️  Copie os arquivos PDF para esta pasta.\n")

    if not PASTA_RESULTADOS.exists():
        PASTA_RESULTADOS.mkdir(parents=True, exist_ok=True)

    ambiente = AmbienteObservable(PASTA_PDFS)

    total = len(list(PASTA_PDFS.glob("*.pdf")))
    if total == 0:
        print("⚠️  Nenhum arquivo PDF encontrado.")
    else:
        print(f"📄 {total} arquivo(s) PDF encontrado(s).")

    return ambiente