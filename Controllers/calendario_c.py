from Models.calendario import Calendario
from Views.calendario_v import CalendarioV
from random import random


class CalendarioC:
    def __init__(self, sistema_c):
        self.__sistema_c = sistema_c
        self.__calendarios = dict()
        self.__calendario = Calendario("00")
        self.__tela = CalendarioV()

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
    def calendario(self, novo_calendario):
        self.__calendario = novo_calendario
    @property
    def sistema_c(self):
        return self.__sistema_c

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

    def puxar_calendario(self, chave: str):
        self.calendario = self.calendarios[chave]
        self.menu(chave)

    def visualizar_eventos(self):
        for evento in self.calendario.eventos.values():
            self.sistema_c.aniversario_c.mostrar_evento(evento)

    def acessar_niver(self):
        niver = self.tela.puxar_data()
        self.sistema_c.aniversario_c.menu(niver)

    def menu(self, chave: str):
        try:
            escolha = int(self.tela.menu_calendario(chave))
        except ValueError:
            self.tela.mensagem("Erro: A opção escolhida deve ser um número inteiro.\nSaindo do sistema...")
            exit(1)
        else:
            match escolha:
                case 1:
                    niver = self.sistema_c.aniversario_c.incluir()
                    self.calendario.eventos[niver.data] = niver
                    self.menu(chave)
                case 2:
                    self.visualizar_eventos()
                    self.menu(chave)
                case 3:
                    self.acessar_niver()
                    self.menu(chave)
                case 0:
                    self.sistema_c.menu()
                case _:
                    exit(0)
