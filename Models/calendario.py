from random import random

class Calendario:
    def __init__(self):
        self.__chave = str(random())[2:]
        self.__eventos = dict()

    @property
    def chave(self):
        return self.__chave

    @property
    def eventos(self):
        return self.__eventos


