

from Views.sistema_v import SistemaV
from Controllers.calendario_c import CalendarioC


class SistemaC:
    def __init__(self):
        self.__calendario = CalendarioC(self)
        self.__tela = SistemaV()

    @property
    def tela(self):
        return self.__tela

    @property
    def calendario(self):
        return self.__calendario

    def criar(self):
        self.calendario.anexar_calendario()

    def visualizar(self):
        self.calendario.puxar_calendario(self.tela.capturar("\nDigite a chave identificadora do calendário: "))

    def imprimir(self):
        self.calendario.imprimir_calendarios()

    def menu(self):
        try:
            escolha = int(self.tela.menu())
        except ValueError:
            self.tela.mensagem("Erro: A opção escolhida deve ser um número inteiro.\nSaindo do sistema...")
            exit()
        else:
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
