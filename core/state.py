from abc import ABC, abstractmethod


class EstadoAmbiente(ABC):
    """
    Interface base para os estados do ambiente.
    """

    @abstractmethod
    def pode_buscar(self) -> bool:
        pass

    @abstractmethod
    def mensagem(self) -> str:
        pass


class AmbienteSemPDFs(EstadoAmbiente):

    def pode_buscar(self) -> bool:
        return False

    def mensagem(self) -> str:
        return (
            "\n❌ A busca está indisponível.\n"
            "➡️  Nenhum arquivo PDF foi encontrado na pasta 'pdfs/'.\n"
            "➡️  Copie os arquivos PDF e realize a busca.\n"
        )


class AmbientePronto(EstadoAmbiente):

    def pode_buscar(self) -> bool:
        return True

    def mensagem(self) -> str:
        return "\n✅ Ambiente pronto para busca.\n"
