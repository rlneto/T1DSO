from Models.academico import Academico
from Views.academico_v import AcademicoV
from Controllers.evento_c import EventoC


class AcademicoC(EventoC):
    def __init__(self, sistema):
        super().__init__(sistema)
        self.__sistema_c = sistema
        self.__tela = AcademicoV()
        self.__evento = None

    @property
    def tela(self):
        return self.__tela

    @property
    def sistema_c(self):
        return self.__sistema_c

    @property
    def evento(self):
        return self.__evento

    @evento.setter
    def evento(self, evento):
        self.__evento = evento

    def incluir(self):
        dados = self.tela.incluir_evento()
        a_evento = Academico(dados[0], dados[1], dados[2], dados[3], dados[4])
        return a_evento

    def alterar(self):
        a_evento = self.evento
        dados = self.tela.alterar_evento()
        a_evento.titulo, a_evento.materia, a_evento.professor, \
            a_evento.descricao = dados[0], dados[1], dados[2], dados[3]
        return a_evento

    def mostrar_evento(self, academico):
        self.tela.mostrar_tudo(academico)

    def menu(self, chave: str):
        self.evento = self.sistema_c.calendario_c.calendario.\
            eventos_academicos[chave]
        escolha = int(self.tela.menu(chave))
        match escolha:
            case 1:
                self.mostrar_evento(self.evento)
                self.menu(chave)
            case 2:
                self.evento = self.alterar()
                self.menu(chave)
            case 3:
                del self.sistema_c.calendario_c.calendario.\
                    eventos_academicos[chave]
                self.sistema_c.calendario_c.menu(self.sistema_c.calendario_c.
                                                 calendario.chave)
            case 0:
                self.sistema_c.calendario_c.menu(self.sistema_c.calendario_c.
                                                 calendario.chave)
            case _:
                exit(0)
