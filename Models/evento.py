from abc import ABC, abstractmethod

class Evento(ABC):
    @abstractmethod
    def __init__(self, data: str = "",  titulo: str = "", descricao: str = ""):
        self.__data = data
        self.__titulo = titulo
        self.__descricao = descricao


    @property
    @abstractmethod
    def data(self):
        return self.__data

    @data.setter
    @abstractmethod
    def data(self, nova_data: str):
        self.__data = nova_data

    @property
    @abstractmethod
    def titulo(self):
        return self.__titulo

    @titulo.setter
    @abstractmethod
    def titulo(self, novo_titulo: str):
        self.__titulo = novo_titulo

    @property
    @abstractmethod
    def descricao(self):
        return self.__descricao

    @descricao.setter
    @abstractmethod
    def descricao(self, nova_descricao: str):
        self.__descricao = nova_descricao
