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
            for item in self.calendarios.values():
                self.tela.listagem(item.chave)
        else:
            self.tela.mensagem("Vazio! Sem calendários no sistema.")

    def puxar_calendario(self, chave: str):
        self.calendario = self.calendarios[chave]
        self.menu(chave)

    def visualizar_eventos(self, tipo: str):
        match tipo:
            case "niver":
                if self.calendario.eventos_aniversarios:
                    for evento in \
                            self.calendario.eventos_aniversarios.values():
                        self.sistema_c.aniversario_c.mostrar_evento(evento)
                else:
                    self.tela.mensagem("Vazio! Sem aniversários no"
                                       " calendário.")
            case "social":
                if self.calendario.eventos_sociais:
                    for evento in self.calendario.eventos_sociais.values():
                        self.sistema_c.social_c.mostrar_evento(evento)
                else:
                    self.tela.mensagem("Vazio! Sem eventos sociais no"
                                       " calendário.")
            case "academico":
                if self.calendario.eventos_academicos:
                    for evento in self.calendario.eventos_academicos.values():
                        self.sistema_c.academico_c.mostrar_evento(evento)
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

    def acessar_eventos(self, tipo: str):
        match tipo:
            case "niver":
                niver = self.tela.puxar_data()
                if self.verificar_chave(1, niver):
                    self.sistema_c.aniversario_c.menu(niver)
                else:
                    self.tela.mensagem("\nNão existe um aniversário com essa"
                                       " data, crie/edite um aniversário ou"
                                       " procure por outra data.\nVoltando às"
                                       " opções do calendário...")
            case "social":
                social = self.tela.puxar_data()
                if self.verificar_chave(2, social):
                    self.sistema_c.social_c.menu(social)
                else:
                    self.tela.mensagem("\nNão existe um evento social com essa"
                                       " data, crie/edite um evento social ou"
                                       " procure por outra data.\nVoltando às"
                                       " opções do calendário...")
            case "academico":
                academico = self.tela.puxar_data()
                if self.verificar_chave(3, academico):
                    self.sistema_c.academico_c.menu(academico)
                else:
                    self.tela.mensagem("\nNão existe um evento academico com"
                                       " essa data, crie/edite um evento"
                                       " academico ou procure por outra data."
                                       "\nVoltando às opções do calendário...")

    def menu(self, chave: str):
        event, value = self.tela.menu_calendario()
        escolha = event
        match escolha:
            case '-IE-':
                self.menu_tipo("incluir")
                self.menu(chave)
            case '-VW-':
                self.menu_tipo("visualizar")
                self.menu(chave)
            case 3:
                self.menu_tipo("acessar")
                self.menu(chave)
            case 4:
                del self.calendarios[chave]
            case '-HOME-':
                self.tela.window.close()
                self.sistema_c.menu()
            case _:
                exit(0)

    def menu_tipo(self, verbo: str):
        r = int(self.tela.tipo_evento(verbo))
        match r:
            case 1:
                if verbo == "incluir":
                    niver = self.sistema_c.aniversario_c.incluir()
                    self.calendario.eventos_aniversarios[niver.data] = niver
                elif verbo == "visualizar":
                    self.visualizar_eventos("niver")
                elif verbo == "acessar":
                    self.acessar_eventos("niver")
            case 2:
                if verbo == "incluir":
                    social = self.sistema_c.social_c.incluir()
                    self.calendario.eventos_sociais[social.data] = social
                elif verbo == "visualizar":
                    self.visualizar_eventos("social")
                elif verbo == "acessar":
                    self.acessar_eventos("social")
            case 3:
                if verbo == "incluir":
                    academico = self.sistema_c.academico_c.incluir()
                    self.calendario.eventos_academicos[academico.data]\
                        = academico
                elif verbo == "visualizar":
                    self.visualizar_eventos("academico")
                elif verbo == "acessar":
                    self.acessar_eventos("academico")
            case 0:
                self.menu()
            case _:
                exit(0)
