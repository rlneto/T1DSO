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
        return self.data

    @data.setter
    @abstractmethod
    def data(self, nova_data: str):
        self.data = nova_data

    @property
    @abstractmethod
    def titulo(self):
        return self.titulo

    @titulo.setter
    @abstractmethod
    def titulo(self, novo_titulo: str):
        self.titulo = novo_titulo

    @property
    @abstractmethod
    def descricao(self):
        return self.descricao

    @descricao.setter
    @abstractmethod
    def descricao(self, nova_descricao: str):
        self.descricao = nova_descricao
