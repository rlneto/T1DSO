from Models.social import Social
from Views.social_v2 import SocialV2
from Controllers.evento_c import EventoC


class SocialC(EventoC):
    def __init__(self, sistema):
        super().__init__(sistema)
        self.__sistema_c = sistema
        self.__tela = SocialV2()
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

    def mostrar_evento(self, sociais):
        dados = []
        for obj in sociais:
            data = obj.data[:2]+'/'+obj.data[-2:]
            dados.append([data, obj.titulo, obj.local, obj.descricao])
        dados = sorted(dados, key=lambda x: (x[0])[-2:])
        if self.tela.listar(dados):
            self.tela.window_tabela.close()

    def incluir(self, dados):
        n_evento = Social(dados[0], dados[1], dados[2], dados[3])
        return n_evento

    def menu(self, chave: str, existe: bool):
        social = None
        if existe:
            self.evento = self.sistema_c.calendario_c.calendario.\
                eventos_sociais[chave]
            dados = self.tela.mostrar_e_incluir(self.evento, chave)
            if dados == "-HOME-":
                self.tela.window.close()
                self.sistema_c.menu()
            else:
                social = self.incluir(dados)
        else:
            dados = self.tela.mostrar_e_incluir(None, chave)
            if dados == "-HOME-":
                self.tela.window.close()
                self.sistema_c.menu()
            else:
                social = self.incluir(dados)

        if social is not None:
            self.sistema_c.calendario_c.calendario.\
                eventos_sociais[social.data] = social
            self.sistema_c.dao.quick_save(self.sistema_c.calendario_c.
                                          calendarios)
            self.tela.mensagem("Salvo!")
            self.tela.window.close()
