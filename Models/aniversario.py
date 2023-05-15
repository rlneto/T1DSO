from Models.evento import Evento


class Aniversario(Evento):

    def __init__(self, data: str, titulo: str, descricao: str):
        super().__init__(data, titulo, descricao)
