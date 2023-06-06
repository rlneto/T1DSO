

from Views.sistema_v2 import SistemaV2
from Controllers.calendario_c import CalendarioC
from Controllers.aniversario_c import AniversarioC
from Controllers.social_c import SocialC
from Controllers.academico_c import AcademicoC


class SistemaC:
    def __init__(self):
        self.__calendario_c = CalendarioC(self)
        self.__aniversario_c = AniversarioC(self)
        self.__social_c = SocialC(self)
        self.__academico_c = AcademicoC(self)
        self.__tela = SistemaV2()
        self.__senha = '123321'

    @property
    def tela(self):
        return self.__tela

    @property
    def calendario_c(self):
        return self.__calendario_c

    @property
    def aniversario_c(self):
        return self.__aniversario_c

    @property
    def social_c(self):
        return self.__social_c

    @property
    def academico_c(self):
        return self.__academico_c

    def criar(self):
        self.calendario_c.anexar_calendario()

    def verificar_chave(self, chave):
        if chave in self.calendario_c.calendarios.keys():
            return True
        else:
            return False

    def visualizar(self, chave: str):
        if self.verificar_chave(chave):
            self.calendario_c.puxar_calendario(chave)
        else:
            self.tela.mensagem("\nNão existe um calendário com essa chave,"
                               " crie um novo calendário ou insira"
                               " outra chave.\nVoltando às opções"
                               " do menu principal...")

    def imprimir(self):
        self.calendario_c.imprimir_calendarios()

    def menu(self):
        event, values = self.tela.menu()
        escolha = 1
        if values['-AC-']:
            escolha = 2
        elif values['-ADM-']:
            escolha = 9


        match escolha:
            case 1:
                self.criar()
                self.menu()
            case 2:
                self.visualizar(values['-KEY-'])
                self.menu()
            case 9:
                if values['-PWD-'] == self.__senha:
                    self.imprimir()
                else:
                    if self.tela.capturar("Senha incorreta, tente novamente:") == self.__senha:
                        self.imprimir()
                    else:
                        self.tela.mensagem("Senha incorreta, voltando ao menu"
                                       " principal...")
                self.menu()
