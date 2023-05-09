from random import random


class Calendario:
    def __init__(self, chave: str):
        self.__chave = chave
        self.__eventos_aniversarios = dict()
        self.__eventos_sociais = dict()
        self.__eventos_academicos = dict()

    @property
    def chave(self):
        return self.__chave

    @property
    def eventos_aniversarios(self):
        return self.__eventos_aniversarios
    @eventos_aniversarios.setter
    def eventos_aniversarios(self, novo_evento):
        self.__eventos_aniversarios = novo_evento

    @property
    def eventos_sociais(self):
        return self.__eventos_sociais
    @eventos_sociais.setter
    def eventos_sociais(self, novo_evento):
        self.__eventos_sociais = novo_evento

    @property
    def eventos_academicos(self):
        return self.__eventos_academicos
    @eventos_academicos.setter
    def eventos_academicos(self, novo_evento):
        self.__eventos_academicos = novo_evento
