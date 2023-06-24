from abc import ABC, abstractmethod


class EventoV2(ABC):
    def __init__(self):
        self.__window = None
        self.__window_tabela = None

    @property
    def window(self):
        return self.__window

    @property
    def window_tabela(self):
        return self.__window_tabela

    @abstractmethod
    def init_components(self, evento, data):
        pass

    @abstractmethod
    def mensagem(self, texto: str):
        pass

    @abstractmethod
    def capturar(self, texto: str):
        pass

    @abstractmethod
    def listar(self, dados):
        pass

    @abstractmethod
    def mostrar_e_incluir(self, academico, data):
        pass
