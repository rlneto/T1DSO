from Models.calendario import Calendario
from Views.calendario_v import CalendarioV
from Controllers.aniversario_c import AniversarioC


class CalendarioC:
    def __init__(self, sistema_c):
        self.__sistema_c = sistema_c
        self.__calendarios = dict()
        self.__calendario = dict()

    @property
    def calendarios(self):
        return self.__calendarios
    @calendarios.setter
    def calendarios(self, calendarios_novos):
        self.__calendarios = calendarios_novos

    @property
    def calendario(self):
        return self.__calendario

    @calendario.setter
    def calendario(self, calendario_novo):
        self.__calendario = calendario_novo

    def criar_calendario(self):
        temporario = self.calendarios.copy()
        temporario[Calendario().chave] = Calendario()
        return temporario

    def anexar_calendario(self):
        self.calendarios = self.criar_calendario()

    def puxar_calendario(self, chave: str) -> ():
        return self.calendarios[chave]
