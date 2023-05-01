from Models.evento import Evento

class Aniversario(Evento):
    def __init__(self, data: str, titulo: str, aniversariante: str,
                 descricao: str = "Sem descrição."):
        super().__init__(data, titulo, descricao)
        self.__aniversariante = aniversariante
