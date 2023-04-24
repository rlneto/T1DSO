from Controllers.evento_c import EventoC
from abc import ABC, abstractmethod


class EventoV(ABC):
    @abstractmethod
    def mostrar_data(self):
        print("\nData: ", EventoC.data)

    @abstractmethod
    def alterar_data(self):
        return str(input("\nInforme a nova data: "))

    @abstractmethod
    def mostrar_titulo(self):
        print("\nTítulo: ", EventoC.titulo)

    @abstractmethod
    def alterar_titulo(self):
        return str(input("\nInforme o novo título: "))

    @abstractmethod
    def mostrar_descricao(self):
        print("\nDescrição: ", EventoC.descricao)

    @abstractmethod
    def alterar_descricao(self):
        return str(input("\nInforme a nova descrição: "))

    def __init__(self):
        pass
