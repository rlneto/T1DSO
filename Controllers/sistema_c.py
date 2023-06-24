
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
        return self.calendario_c.anexar_calendario()

    def verificar_chave(self, chave):
        if chave in self.calendario_c.calendarios.keys():
            return True
        else:
            return False

    def visualizar(self, chave: str):
        if self.verificar_chave(chave):
            self.tela.window.close()
            self.calendario_c.puxar_calendario(chave)
        else:
            self.tela.mensagem("\nNão existe calendário com essa chave,\
                                crie um novo calendário ou insira outra chave."
                               "\nVoltando às opções do menu principal...")

    def imprimir(self):
        self.tela.window.close()
        self.calendario_c.imprimir_calendarios()

    def menu(self):
        event, values = self.tela.menu()
        print(event, values)
        escolha = event
        match escolha:
            case '-CC-':
                chaves = self.criar()
                self.tela.mensagem(("Calendário criado com sucesso!\nChave: "
                                    + chaves[0] + "\nSenha de Admin: "
                                    + chaves[1]))
                self.tela.window.close()
                self.menu()
            case '-AC-':
                chave = self.tela.capturar("chave do calendario")
                self.visualizar(chave)
                self.tela.window.close()
                self.menu()
            case '-DEV-':
                senha = self.tela.capturar("senha de desenvolvedor")
                if senha == self.__senha:
                    self.imprimir()
                else:
                    if self.tela.capturar("Senha incorreta,\
                                           tente novamente:") == self.__senha:
                        self.imprimir()
                    else:
                        self.tela.mensagem("Senha incorreta,\
                                            voltando ao menu principal...")
                self.tela.window.close()
                self.menu()
            case _:
                exit()
