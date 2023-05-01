from Views.sistema_v import SistemaV
from Controllers.calendario_c import CalendarioC


class SistemaC:
    def __init__(self):
        self.calendario_c = CalendarioC(self)

