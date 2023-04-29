from Models.calendario import Calendario

class CalendarioC:
    def __init__(self, sistema_c):
        self.__calendarios = None
        self.__sistema_c = sistema_c

    @property
    def calendarios(self):
        return self.__calendarios
    @calendarios.setter
    def calendarios(self, calendarios_novos):
        self.__calendarios = calendarios_novos

    def criar_calendario(self, calendarios):
        pass