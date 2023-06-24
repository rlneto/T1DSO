from Models.calendario import Calendario
from Views.calendario_v import CalendarioV
from Views.calendario_v2 import CalendarioV2
from random import random


class CalendarioC:
    def __init__(self, sistema_c):
        self.__sistema_c = sistema_c
        self.__calendarios = dict()
        self.__calendario = Calendario("00", "00")
        self.__tela = CalendarioV2()

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
        senha_adm = str(random())[2:4]
        if chave not in temporario.keys():
            temporario[chave] = Calendario(chave, senha_adm)
            return temporario, chave, senha_adm
        else:
            return self.criar_calendario()

    def anexar_calendario(self):
        criar = self.criar_calendario()
        self.calendarios = criar[0].copy()
        return criar[1], criar[2]

    def imprimir_calendarios(self) -> str:
        if self.calendarios:
            retorno = set()
            for item in self.calendarios.values():
                retorno.add(item.chave)
            palavra = "Relação de calendários no sistema\n"
            for chave in retorno:
                palavra = palavra + "\nChave: " + chave
            return palavra
        else:
            return "Vazio! Sem calendários no sistema."

    def puxar_calendario(self, chave: str):
        self.calendario = self.calendarios[chave]
        self.menu(chave)


    def menu(self, chave: str):
        event, values = self.tela.menu()
        print(event, values)
        escolha = '-EXIT-'
        for dupla in values.items():
            if dupla[1]:
                escolha = dupla[0]
        match escolha:
            case '-IE-':
                novo_evento = self.tela.incluir_evento(values['-TIPO-'])
                self.menu(chave)
            case '-VW-':
                listagem = 'Relação de eventos:\n'
                for evento in self.calendarios[chave].items():
                    listagem = listagem + "\n" + evento(0) + ":" + evento(1)
                self.tela.mensagem(listagem)
                self.menu(chave)
            case '-HOME-':

                self.menu(chave)
            case '-DEL-':
                pass
            case '-HOME-':
                self.sistema_c.menu()
            case _:
                exit(0)
