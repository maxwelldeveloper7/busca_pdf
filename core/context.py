from core.state import AmbientePronto, AmbienteSemPDFs, EstadoAmbiente


class AmbienteContexto:
    """
    Contexto responsável por manter o estado atual do ambiente.
    """

    def __init__(self, total_pdfs: int) -> None:
        self.estado: EstadoAmbiente

        if total_pdfs == 0:
            self.estado = AmbienteSemPDFs()
        else:
            self.estado = AmbientePronto()

    def pode_buscar(self) -> bool:
        return self.estado.pode_buscar()

    def mensagem(self) -> str:
        return self.estado.mensagem()
