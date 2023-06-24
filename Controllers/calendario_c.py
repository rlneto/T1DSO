from Models.calendario import Calendario
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

    def imprimir_calendarios(self):
        if self.calendarios:
            print(self.calendarios)
            dados = []
            for obj in self.calendarios.values():
                dados.append([obj.chave,
                              obj.chave_adm, obj])
            self.sistema_c.tela.listar_calendarios(dados)
        else:
            self.tela.mensagem("Vazio! Sem calendários no sistema.")

    def puxar_calendario(self, chave: str):
        self.calendario = self.calendarios[chave]
        self.menu(chave)

    def visualizar_eventos(self, tipo: str):
        match tipo:
            case "niver":
                if self.calendario.eventos_aniversarios:
                    aniversarios = self.calendario.\
                        eventos_aniversarios.values()
                    self.sistema_c.aniversario_c.mostrar_evento(aniversarios)
                else:
                    self.tela.mensagem("Vazio! Sem aniversários no"
                                       " calendário.")
            case "social":
                if self.calendario.eventos_sociais:
                    sociais = self.calendario.eventos_sociais.values()
                    self.sistema_c.social_c.mostrar_evento(sociais)
                else:
                    self.tela.mensagem("Vazio! Sem eventos sociais no"
                                       " calendário.")
            case "academico":
                if self.calendario.eventos_academicos:
                    academicos = self.calendario.eventos_academicos.values()
                    self.sistema_c.academico_c.mostrar_evento(academicos)
                else:
                    self.tela.mensagem("Vazio! Sem eventos academicos no"
                                       " calendário.")

    def verificar_chave(self, tipo, chave):
        match tipo:
            case 1:
                evento_chave = self.calendario.eventos_aniversarios.keys()
            case 2:
                evento_chave = self.calendario.eventos_sociais.keys()
            case 3:
                evento_chave = self.calendario.eventos_academicos.keys()
        if chave in evento_chave:
            return True
        else:
            return False
    ###############################################
    ###############################################

    def menu(self, chave: str):
        event, value = self.tela.menu_calendario()
        escolha = event
        match escolha:
            case '-IE-':
                self.menu_tipo("acessar")
                self.menu(chave)
            case '-VW-':
                self.menu_tipo("visualizar")
                self.menu(chave)
            case '-HOME-':
                self.tela.window.close()
                self.sistema_c.menu()
            case '-DEL-':
                if self.tela.capturar('senha') == self.calendario.chave_adm:
                    del self.calendarios[self.calendario.chave]

    def menu_tipo(self, verbo: str):
        self.tela.window.close()
        values = self.tela.tipo_evento()
        escolha = None
        if values is not None:
            for dupla in values.items():
                if dupla[1]:
                    escolha = int(dupla[0])
        match escolha:
            case 1:
                if verbo == "acessar":
                    data = self.tela.puxar_data()
                    self.tela.window_data.close()
                    self.tela.window.close()
                    self.sistema_c.aniversario_c.\
                        menu(data, self.verificar_chave(1, data))
                elif verbo == "visualizar":
                    self.visualizar_eventos("niver")
            case 2:
                if verbo == "acessar":
                    self.tela.window_tipo.close()
                    data = self.tela.puxar_data()
                    self.tela.window_data.close()
                    self.sistema_c.social_c.\
                        menu(data, self.verificar_chave(1, data))
                elif verbo == "visualizar":
                    self.visualizar_eventos("social")
            case 3:
                if verbo == "acessar":
                    self.tela.window_tipo.close()
                    data = self.tela.puxar_data()
                    self.tela.window_data.close()
                    self.sistema_c.academico_c.\
                        menu(data, self.verificar_chave(1, data))
                elif verbo == "visualizar":
                    self.visualizar_eventos("academico")
