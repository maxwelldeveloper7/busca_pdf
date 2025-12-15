# ------------------------------------------------------------------------------
# Função: buscar_nos_pdfs
# Percorre todos os arquivos PDF da pasta especificada e busca o termo informado.
# ------------------------------------------------------------------------------
import os
from tqdm import tqdm
import pdfplumber

PASTA_PDFS = "pdfs"


def buscar_nos_pdfs(termo_busca: str) -> list[dict]:
    """
    Busca o termo especificado em todos os arquivos PDF na pasta definida.
    Args:
        termo_busca (str): O termo a ser buscado nos PDFs.
    Returns:
        Retorna uma lista de dicionários com as ocorrências encontradas.
    """
    termo_busca = termo_busca.lower()
    resultados: list[dict] = []

    arquivos_pdf = [
        arq for arq in os.listdir(PASTA_PDFS) if arq.endswith(".pdf")
    ]

    total_paginas = 0
    for arquivo in arquivos_pdf:
        try:
            with pdfplumber.open(os.path.join(PASTA_PDFS, arquivo)) as pdf:
                total_paginas += len(pdf.pages)
        except FileNotFoundError:
            continue

    with tqdm(
        total=total_paginas,
        desc=f"Procurando por '{termo_busca}'",
        unit="páginas",
        ncols=80,
        # colour='green',
        bar_format="{desc}:{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} {unit}"
    ) as barra:

        for arquivo in arquivos_pdf:
            try:
                with pdfplumber.open(os.path.join(PASTA_PDFS, arquivo)) as pdf:
                    for i, pagina in enumerate(pdf.pages, start=1):
                        texto = pagina.extract_text() or ""
                        texto_lower = texto.lower()

                        if termo_busca in texto_lower:
                            pos = texto_lower.find(termo_busca)
                            contexto = texto[max(0, pos - 50):pos + len(termo_busca) + 50]

                            resultados.append({
                                "arquivo": arquivo,
                                "pagina": i,
                                "contexto": contexto.replace("\n", " ").strip()
                            })

                        barra.update(1)
            except FileNotFoundError:
                continue

    return resultados
