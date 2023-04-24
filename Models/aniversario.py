from evento import Evento
from calendario import Calendario

class Aniversario(Evento):
    def __init__(self, calendario: Calendario(), data: str, titulo: str, aniversariante: str,
                 descricao: str = "Sem descrição."):
        super().__init__(calendario, data, titulo, descricao)
        self.__aniversariante = aniversariante
