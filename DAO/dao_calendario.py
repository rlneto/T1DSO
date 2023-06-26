import pickle as pickle


class DAOCalendario:
    def __init__(self, cache=None, datasource='calendarios.pkl'):
        if cache is None:
            cache = {}
        self.__datasource = datasource
        self.__cache = cache
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

    def load(self, chave: str) -> dict:
        self.__load()
        return self.__cache[chave]

    def quick_load(self) -> dict:
        self.__load()
        print(self.__cache)
        return self.__cache

    def quick_save(self, calendarios: dict):
        self.__cache = calendarios
        self.__dump()
