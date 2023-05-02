from Models.calendario import Calendario
from Views.calendario_v import CalendarioV
from Controllers.aniversario_c import AniversarioC
from random import random


class CalendarioC:
    def __init__(self, sistema_c):
        self.__sistema_c = sistema_c
        self.__calendarios = dict()
        self.__calendario = dict()
        self.__tela = CalendarioV()
        self.__aniversario = AniversarioC(self)

    @property
    def tela(self):
        return self.__tela

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
        chave = str(random())[2:4]
        if chave not in temporario.keys():
            temporario[chave] = Calendario(chave)
            self.tela.sucesso(chave)
            return temporario
        else:
            return self.criar_calendario()


    def anexar_calendario(self):
        self.calendarios = self.criar_calendario()

    def imprimir_calendarios(self):
        for item in self.calendarios.values():
            self.tela.listagem(item.chave)
    def menu(self, chave: str):
        try:
            escolha = int(self.tela.menu_calendario(chave))
        except ValueError:
            self.tela.mensagem("Erro: A opção escolhida deve ser um número inteiro.\nSaindo do sistema...")
            exit()
        else:
            match escolha:
                case 1:
                    pass
                case _:
                    exit(0)

    def puxar_calendario(self, chave: str) -> ():
        self.calendario = self.calendarios[chave]
        self.menu(chave)

    # def visualizar_eventos(self):
    #     for evento in self.calendario.items():

