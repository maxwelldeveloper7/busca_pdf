"""Módulo utilitário para destacar termos em textos."""
import re


def destacar_termo(contexto: str, termo: str) -> str:
    """
    Procura o termo em todo o contexto e aplica cor ANSI a todas as ocorrências.
    A busca é case-insensitive e preserva o texto original.
    | Cor      | Código ANSI             |
    | -------- | ------------------------|
    | Vermelho | `\033[1;31m`            |
    | Verde    | `\033[1;32m`            |
    | Amarelo  | `\033[1;33m`            |
    | Azul     | `\033[1;34m`            |
    | Magenta  | `\033[1;35m`            |
    | Ciano    | `\033[1;36m`            |
    | Camarelo | `\033[38;2;205;133;63m` |
    """
    if not termo:
        return contexto

    padrao = re.compile(re.escape(termo), re.IGNORECASE)
    inicio = "\033[38;2;205;133;63m"
    fim = "\033[0m"

    return padrao.sub(lambda m: f"{inicio}{m.group(0)}{fim}", contexto)
