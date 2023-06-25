import pickle as pickle
from abc import ABC


class DAO(ABC):
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        with open(self.__datasource, 'wb') as arquivo:
            pickle.dump(self.__cache, arquivo)

    def __load(self):
        with open(self.__datasource, 'rb') as arquivo:
            self.__cache = pickle.load(arquivo)

