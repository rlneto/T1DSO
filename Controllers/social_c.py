from Models.social import Social
from Views.social_v import SocialV
from Controllers.evento_c import EventoC


class SocialC(EventoC):
    def __init__(self, sistema):
        super().__init__(sistema)
        self.__sistema_c = sistema
        self.__tela = SocialV()
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
        s_evento = Social(dados[0], dados[1], dados[2], dados[3])
        return s_evento

    def alterar(self):
        s_evento = self.evento
        dados = self.tela.alterar_evento()
        s_evento.titulo,s_evento.local, s_evento.descricao = dados[0], dados[1], dados[2]
        return s_evento

    def mostrar_evento(self, social):
        self.tela.mostrar_tudo(social)

    def menu(self, chave: str):
        self.evento = self.sistema_c.calendario_c.calendario.eventos_sociais[chave]
        try:
            escolha = int(self.tela.menu(chave))
        except ValueError:
            self.tela.mensagem("Erro: A opção escolhida deve ser um número inteiro.\nSaindo do sistema...")
            exit(1)
        else:
            match escolha:
                case 1:
                    self.mostrar_evento(self.evento)
                    self.menu(chave)
                case 2:
                    self.evento = self.alterar()
                    self.menu(chave)
                case 3:
                    del self.sistema_c.calendario_c.calendario.eventos_sociais[chave]
                    self.sistema_c.calendario_c.menu(self.sistema_c.calendario_c.calendario.chave)
                case 0:
                    self.sistema_c.calendario_c.menu(self.sistema_c.calendario_c.calendario.chave)
                case _:
                    exit(0)
