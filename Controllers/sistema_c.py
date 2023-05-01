

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
        self.calendario.puxar_calendario(input("\nDigite a chave identificadora do calendário: "))

    def menu(self):
        try:
            match int(self.tela.menu()):
                case 1:
                    self.criar()
                    self.menu()
                case 2:
                    self.visualizar()
                case 0:
                    print("Saindo do sistema...")
                    exit(0)
                case _:
                    print("\nOpção inválida, tente novamente.\n")
                    self.menu()
        except ValueError:
            print("Erro: A opção escolhida deve ser um número inteiro.\nSaindo do sistema...")
            exit()

