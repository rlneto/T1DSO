from Models.aniversario import Aniversario
from Views.aniversario_v2 import AniversarioV2
from Controllers.evento_c import EventoC


class AniversarioC(EventoC):
    def __init__(self, sistema):
        super().__init__(sistema)
        self.__sistema_c = sistema
        self.__tela = AniversarioV2()
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

    def mostrar_evento(self, aniversarios):
        dados = []
        for obj in aniversarios:
            data = obj.data[:2]+'/'+obj.data[-2:]
            dados.append([data, obj.titulo, obj.descricao])
        dados = sorted(dados, key=lambda x: (x[0])[-2:])
        self.tela.listar(dados)

    def incluir(self, dados):
        n_evento = Aniversario(dados[0], dados[1], dados[2])
        return n_evento

    def menu(self, chave: str, existe: bool):
        niver = None
        if existe:
            self.evento = self.sistema_c.calendario_c.calendario.\
                eventos_aniversarios[chave]
            dados = self.tela.mostrar_e_incluir(self.evento, chave)
            if dados == "-HOME-":
                self.tela.window.close()
                self.sistema_c.menu()
            else:
                niver = self.incluir(dados)
        else:
            dados = self.tela.mostrar_e_incluir(None, chave)
            if dados == "-HOME-":
                self.tela.window.close()
                self.sistema_c.menu()
            else:
                niver = self.incluir(dados)
        
        if niver is not None:
            self.sistema_c.calendario_c.calendario.\
                eventos_aniversarios[niver.data] = niver
            self.tela.mensagem("Salvo!")
            self.tela.window.close()
