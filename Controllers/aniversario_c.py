from Models.aniversario import Aniversario
from Views.aniversario_v import AniversarioV
from Controllers.evento_c import EventoC


class AniversarioC(EventoC):
    def __init__(self, sistema):
        super().__init__(sistema)
        self.__sistema_c = sistema
        self.__tela = AniversarioV()
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
        n_evento = Aniversario(dados[0], dados[1], dados[2])
        return n_evento

    def alterar(self):
        n_evento = self.evento
        dados = self.tela.alterar_evento()
        n_evento.titulo, n_evento.descricao = dados[0], dados[1]
        return n_evento

    def mostrar_evento(self, aniversario):
        self.tela.mostrar_tudo(aniversario)

    def menu(self, chave: str):
        self.evento = self.sistema_c.calendario_c.calendario.eventos_aniversarios[chave]
        escolha = int(self.tela.menu(chave))
        match escolha:
            case 1:
                self.mostrar_evento(self.evento)
                self.menu(chave)
            case 2:
                self.evento = self.alterar()
                self.menu(chave)
            case 3:
                del self.sistema_c.calendario_c.calendario.eventos_aniversarios[chave]
                self.sistema_c.calendario_c.menu(self.sistema_c.calendario_c.calendario.chave)
            case 0:
                self.sistema_c.calendario_c.menu(self.sistema_c.calendario_c.calendario.chave)
            case _:
                exit(0)
