from Models.evento import Evento
from abc import ABC, abstractmethod


class EventoC(ABC):
    @abstractmethod
    def __init__(self, calendario):
        self.__calendario = calendario
        self.__tela = None
        self.__evento = None

    @property
    @abstractmethod
    def tela(self):
        return self.__tela

    @property
    @abstractmethod
    def calendario(self):
        return self.__calendario

    @property
    @abstractmethod
    def evento(self):
        return self.__evento

    @evento.setter
    @abstractmethod
    def evento(self, evento):
        self.__evento = evento

    @abstractmethod
    def incluir(self):
        dados = self.tela.incluir_evento()
        n_evento = Evento(dados[0], dados[1], dados[2])
        return n_evento

    @abstractmethod
    def alterar_data(self):
        self.evento.data = self.tela.alterar_data

    @abstractmethod
    def alterar_titulo(self):
        self.evento.titulo = self.tela.alterar_titulo

    @abstractmethod
    def alterar_descricao(self):
        self.evento.descricao = self.tela.alterar_descricao
