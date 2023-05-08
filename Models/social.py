from Models.evento import Evento


class Social(Evento):

    def __init__(self, data: str, titulo: str, local: str, descricao: str = "Sem descrição."):
        super().__init__(data, titulo, descricao)
        self.__local = local

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, novo_local: str):
        self.__local = novo_local