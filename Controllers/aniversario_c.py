from Models.aniversario import Aniversario
from Views.aniversario_v import AniversarioV
from Controllers.evento_c import EventoC


class AniversarioC(EventoC):
    def __init__(self, calendario):
        super().__init__(calendario)
        self.__calendario = calendario
        self.__tela = AniversarioV()
        self.__evento = None

    @property
    def tela(self):
        return self.__tela

    @property
    def calendario(self):
        return self.__calendario

    @property
    def evento(self):
        return self.__evento

    @evento.setter
    def evento(self, evento):
        self.__evento = evento

    def incluir(self):
        dados = self.tela.incluir_evento()
        n_evento = Aniversario(dados[0], dados[1], dados[2])
        return n_evento

    def alterar_data(self):
        self.evento.data = self.tela.alterar_data

    def alterar_titulo(self):
        self.evento.titulo = self.tela.alterar_titulo

    def alterar_descricao(self):
        self.evento.descricao = self.tela.alterar_descricao

    def mostrar_evento(self, aniversario):
        self.tela.mostrar_tudo(aniversario)
