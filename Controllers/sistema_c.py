

from Views.sistema_v import SistemaV
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
        self.__tela = SistemaV()

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

    def visualizar(self):
        self.calendario_c.puxar_calendario(self.tela.capturar("\nDigite a chave identificadora do calendário: "))

    def imprimir(self):
        self.calendario_c.imprimir_calendarios()

    def menu(self):
        escolha = self.tela.menu()
        match escolha:
            case 1:
                self.criar()
                self.menu()
            case 2:
                self.visualizar()
                self.menu()
            case 9:
                self.imprimir()
                self.menu()
            case 0:
                self.tela.mensagem("Saindo do sistema...")
                exit(0)
            case _:
                self.tela.mensagem("\nOpção inválida, tente novamente.\n")
                self.menu()
