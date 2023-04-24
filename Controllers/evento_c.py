from Models.calendario import Calendario
from Models.evento import Evento
from Views.evento_v import EventoV
from abc import ABC, abstractmethod


class EventoC(ABC):
    @abstractmethod
    def alterar_data(self):
        self.evento.data = EventoV.alterar_data

    @abstractmethod
    def alterar_titulo(self):
        self.evento.titulo = EventoV.alterar_titulo

    @abstractmethod
    def alterar_descricao(self):
        self.evento.descricao = EventoV.alterar_descricao

    def __init__(self, calendario: Calendario, evento: Evento):
        self.__calendario = calendario
        self.__evento = evento

    @property
    def evento(self):
        return self.__evento

    @property
    def calendario(self):
        return self.evento.calendario

    @property
    def data(self):
        return self.evento.data

    @data.setter
    def data(self, nova_data: str):
        self.evento.data = nova_data

    @property
    def titulo(self):
        return self.evento.titulo

    @titulo.setter
    def titulo(self, novo_titulo: str):
        self.evento.titulo = novo_titulo

    @property
    def descricao(self):
        return self.evento.descricao

    @descricao.setter
    def descricao(self, nova_descricao: str):
        self.evento.descricao = nova_descricao
