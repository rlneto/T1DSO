from Views.sistema_v import SistemaV
from Controllers.calendario_c import CalendarioC
from Controllers.evento_c import EventoC
from Controllers.aniversario_c import AniversarioC

class SistemaC:
    def __init__(self):
        self.calendario_c = CalendarioC(self)
        self.aniversario_c = AniversarioC()

