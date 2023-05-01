from random import random

class Calendario:
    def __init__(self, chave: str):
        self.__chave = chave
        self.__eventos = dict()

    @property
    def chave(self):
        return self.__chave

    @property
    def eventos(self):
        return self.__eventos


