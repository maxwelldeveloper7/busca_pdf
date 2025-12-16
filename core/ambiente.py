from pathlib import Path
from core.observer import Subject, Observer
from core.context import AmbienteContexto


class AmbienteObservable(Subject):
    """
    Ambiente observável que monitora a pasta de PDFs.
    """

    def __init__(self, pasta_pdfs: Path):
        self._pasta_pdfs = pasta_pdfs
        self._observers: list[Observer] = []
        self.contexto = self._avaliar_estado()

    def registrar(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notificar(self) -> None:
        for observer in self._observers:
            observer.atualizar()

    def _avaliar_estado(self) -> AmbienteContexto:
        total_pdfs = len(list(self._pasta_pdfs.glob("*.pdf")))
        return AmbienteContexto(total_pdfs)

    def verificar_pdfs(self) -> None:
        """
        Reavalia a pasta pdfs e notifica observadores se necessário.
        """
        self.contexto = self._avaliar_estado()
        self.notificar()

    def total_pdfs(self) -> int:
        """
        Retorna a quantidade atual de PDFs sem notificar observadores.
        """
        return len(list(self._pasta_pdfs.glob("*.pdf")))
