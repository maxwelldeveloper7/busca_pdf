# ------------------------------------------------------------------------------
# Função: registrar_log
# Salva as ocorrências encontradas em um arquivo de log.
# ------------------------------------------------------------------------------
from datetime import datetime
import os

PASTA_RESULTADOS = "resultados"
ARQUIVO_LOG = os.path.join(PASTA_RESULTADOS, "logs_pesquisa.txt")


def registrar_log(termo: str, resultados: list[dict]) -> None:
    """"
    Registra o log da pesquisa em um arquivo de texto.
    Args:
        termo (str): O termo pesquisado.
        resultados (list[dict]): Lista de dicionários com as ocorrências encontradas.
    """
    os.makedirs(PASTA_RESULTADOS, exist_ok=True)

    with open(ARQUIVO_LOG, "a", encoding="utf-8") as log:
        log.write("\n" + "=" * 80 + "\n")
        log.write(f"Pesquisa realizada em: {datetime.now():%d/%m/%Y %H:%M:%S}\n")
        log.write(f"Termo pesquisado: {termo}\n")
        log.write(f"Total de ocorrências: {len(resultados)}\n\n")

        for r in resultados:
            log.write(
                f"Arquivo: {r['arquivo']} | Página: {r['pagina']}\n"
                f"Contexto: ...{r['contexto']}...\n\n"
            )
