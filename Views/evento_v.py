from abc import ABC, abstractmethod


class EventoV(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def mostrar_data(self, data):
        print("\nData: ", data)


    @abstractmethod
    def mostrar_titulo(self, titulo):
        print("\nTítulo: ", titulo)


    @abstractmethod
    def mostrar_descricao(self, descricao):
        print("\nDescrição: ", descricao)

    @abstractmethod
    def incluir_evento(self) -> tuple:
        pass

    @abstractmethod
    def mensagem(self, message: str):
        pass

    @abstractmethod
    def capturar(self, message) ->str:
        pass

    @abstractmethod
    def alterar_evento(self) ->tuple:
        pass

    @abstractmethod
    def menu(self) ->int:
        pass

