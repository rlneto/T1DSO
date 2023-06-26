
from Views.sistema_v2 import SistemaV2
from Controllers.calendario_c import CalendarioC
from Controllers.aniversario_c import AniversarioC
from Controllers.social_c import SocialC
from Controllers.academico_c import AcademicoC
from DAO.dao_calendario import DAOCalendario


class SistemaC:
    def __init__(self):
        self.__dao_c = DAOCalendario()
        self.__calendario_c = CalendarioC(self)
        self.__aniversario_c = AniversarioC(self)
        self.__social_c = SocialC(self)
        self.__academico_c = AcademicoC(self)
        self.__tela = SistemaV2()
        self.__senha = '123321'

    @property
    def dao(self):
        return self.__dao_c

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
        try:
            chave_teste = int(chave)
        except TypeError:
            self.tela.mensagem('Tipo inválido, tente novamente.')
        except ValueError:
            self.tela.mensagem('Valor inválido ,tente novamente.')
        else:
            if self.verificar_chave(chave):
                self.tela.window.close()
                self.calendario_c.puxar_calendario(chave)
            else:
                self.tela.mensagem("Não existe calendário com essa chave,\
                                    crie um novo calendário ou insira outra\
                                    chave.""\nVoltando às opções do menu\
                                    principal...")

    def imprimir(self):
        self.tela.window.close()
        self.calendario_c.imprimir_calendarios()

    def menu(self):
        event, values = self.tela.menu()
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
                botao, chave = self.tela.capturar("chave do calendario")
                chave = chave['-TEXTO-']
                if botao == 'OK':
                    self.visualizar(chave)
                    self.tela.window.close()
                    self.menu()
                else:
                    self.tela.window.close()
                    self.menu()
            case '-DEV-':
                entrada = self.tela.capturar("senha de desenvolvedor")
                if (entrada[0] == 'OK' and
                        entrada[1]['-TEXTO-'] == self.__senha):
                    self.imprimir()
                else:
                    if entrada[0] == 'OK':
                        entrada = self.tela.capturar("Senha incorreta,\
                                                     tente novamente")
                        if (entrada[0] == 'OK' and
                                entrada[1]['-TEXTO-'] == self.__senha):
                            self.imprimir()
                        elif entrada[0] == 'OK':
                            self.tela.mensagem("Senha incorreta, voltando ao\
                                               menu principal...")
                self.tela.window.close()
                self.menu()
            case _:
                exit()
