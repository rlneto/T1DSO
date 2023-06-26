from Models.academico import Academico
from Views.academico_v2 import AcademicoV2
from Controllers.evento_c import EventoC


class AcademicoC(EventoC):
    def __init__(self, sistema):
        super().__init__(sistema)
        self.__sistema_c = sistema
        self.__tela = AcademicoV2()
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

    def mostrar_evento(self, academicos):
        dados = []
        for obj in academicos:
            data = obj.data[:2]+'/'+obj.data[-2:]
            dados.append([data, obj.titulo, obj.materia, obj.professor,
                         obj.descricao])
        dados = sorted(dados, key=lambda x: (x[0])[-2:])
        if self.tela.listar(dados):
            self.tela.window_tabela.close()

    def incluir(self, dados):
        n_evento = Academico(dados[0], dados[1], dados[2], dados[3], dados[4])
        return n_evento

    def menu(self, chave: str, existe: bool):
        academico = None
        if existe:
            self.evento = self.sistema_c.calendario_c.calendario.\
                eventos_academicos[chave]
            dados = self.tela.mostrar_e_incluir(self.evento, chave)
            if dados == "-HOME-":
                self.tela.window.close()
                self.sistema_c.menu()
            else:
                academico = self.incluir(dados)
        else:
            dados = self.tela.mostrar_e_incluir(None, chave)
            if dados == "-HOME-":
                self.tela.window.close()
                self.sistema_c.menu()
            else:
                academico = self.incluir(dados)

        if academico is not None:
            self.sistema_c.calendario_c.calendario.\
                eventos_academicos[academico.data] = academico
            self.sistema_c.dao.quick_save(self.sistema_c.calendario_c
                                          .calendarios)
            self.tela.mensagem("Salvo!")
            self.tela.window.close()
