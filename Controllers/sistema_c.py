from Views.sistema_v import SistemaV
from Controllers.calendario_c import CalendarioC
import json


def carregar_db() -> dict:
    with open("dados.json", "r") as arquivo:
        cals = json.load(arquivo)
        # print(cals)
        # for item in cals.items():
        #     print(item)
        #     for subitem in item[1].items():
        #         print(subitem)
        #         for microitem in subitem[1].items():
        #             print(microitem)
        return cals




class SistemaC:

    def carrega_cals(self, cals: dict):
        for item in self.__cals.values():
            # print(item)
            for subitem in item.values():
                self.calendario.calendarios[subitem["data"]] = self.calendario.calendario.
                self.calendario.calendarios[subitem["data"]]
    def __init__(self):
        self.__tela = SistemaV()
        self.__cals = carregar_db()
        self.__calendario = CalendarioC(self)
        self.carrega_cals(self.__cals)

    @property
    def tela(self):
        return self.__tela

    @property
    def cals(self):
        return self.__cals

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
            exit(1)
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
                    # saida = dict()
                    # for item in self.calendario.calendarios.items():
                    #     print(item[0])
                    #     print(item[1])
                    #     saida[item[0]][item[1].data] = dict()
                    #     saida[item[0]][item[1].data]["data"] = evento.data
                    #     saida[item[0]][item[1].data]["titulo"] = evento.titulo
                    #     saida[item[0]][item[1].data]["descricao"] = evento.descricao
                    with open("dados.json", "w") as arquivo:
                        saida = dict()
                        for item in self.calendario.calendarios.items():
                            saida[item[0]] = dict()
                            for evento in item[1].eventos.values():
                                saida[item[0]][evento.data] = dict()
                                saida[item[0]][evento.data]["data"] = evento.data
                                saida[item[0]][evento.data]["titulo"] = evento.titulo
                                saida[item[0]][evento.data]["descricao"] = evento.descricao
                        json.dump(saida, arquivo)
                    self.tela.mensagem("Saindo do sistema...")
                    exit(0)
                case _:
                    self.tela.mensagem("\nOpção inválida, tente novamente.\n")
                    self.menu()
