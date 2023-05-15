from Models.evento import Evento


class Academico(Evento):

    def __init__(self, data: str, titulo: str, materia: str, professor: str,
                 descricao: str):
        super().__init__(data, titulo, descricao)
        self.__materia = materia
        self.__professor = professor

    @property
    def materia(self):
        return self.__materia

    @materia.setter
    def materia(self, nova_materia: str):
        self.__materia = nova_materia

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, novo_professor: str):
        self.__professor = novo_professor
