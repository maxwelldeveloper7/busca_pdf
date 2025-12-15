"""Módulo utilitário para operações relacionadas ao terminal."""


def limpar_terminal() -> None:
    """Limpa o terminal."""
    print("\033[H\033[J", end="")
