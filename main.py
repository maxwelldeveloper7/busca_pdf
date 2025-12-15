"""
Aplicativo de Busca em Múltiplos Arquivos PDF
Autor: Maxwell de Oliveira Chaves
Versão: 1.1
Descrição:
    Este aplicativo realiza buscas textuais em todos os arquivos PDF
    contidos em uma pasta local, exibindo e registrando as ocorrências
    encontradas. O sistema foi desenvolvido em Python com foco em uso
    pedagógico, facilitando a pesquisa de conteúdos e acessibilidade para avaliações
    educacionais online.
"""
from utils.bootstrap import inicializar_ambiente
from cli.menu import exibir_menu


def main() -> None:
    """   
    Função principal do aplicativo.
    Inicializa o ambiente e exibe o menu principal.
    """
    total_pdfs = inicializar_ambiente()
    exibir_menu(total_pdfs)


if __name__ == "__main__":
    main()
