from random import random

class Calendario:
    def __init__(self, codigo: str):
        self.__chave = str(random())[2:]
        self.__eventos = set()
