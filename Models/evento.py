from .calendario import Calendario
from abc import ABC

class Evento(ABC):
    def __init__(self, calendario: Calendario(), data: str, titulo: str, descricao: str = "Sem descrição."):
        self.__calendario = calendario
        self.__data = data
        self.__titulo = titulo
        self.__descricao = descricao

    @property
    def calendario(self):
        return self.__calendario

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, nova_data: str):
        self.__data = nova_data

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo: str):
        self.__titulo = novo_titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao: str):
        self.__descricao = nova_descricao
