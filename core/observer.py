from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def atualizar(self) -> None:
        pass


class Subject(ABC):

    @abstractmethod
    def registrar(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notificar(self) -> None:
        pass
