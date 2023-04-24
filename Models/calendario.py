from random import random

class Calendario:
    def __init__(self):
        self.__chave = str(random())[2:]
        self.__eventos = set()
