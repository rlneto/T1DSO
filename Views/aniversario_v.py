from Views.evento_v import EventoV


class AniversarioV(EventoV):
    def mostrar_data(self, data):
        print("\nData: ", data)

    def alterar_data(self):
        return str(input("\nInforme a nova data de aniversário: "))

    def mostrar_titulo(self, titulo):
        print("\nTítulo: ", titulo)

    def alterar_titulo(self):
        return str(input("\nInforme o aniversariante: "))

    def mostrar_descricao(self, descricao):
        print("\nDescrição: ", descricao)

    def alterar_descricao(self):
        return str(input("\nInforme a nova descrição: "))

    def incluir_evento(self) -> tuple:
        dia = input("\nInforme o dia do aniversário: ")
        mes = input("\nAgora, informe o mês do aniversário: ")
        data = dia+mes
        dia, mes = None, None
        titulo = input("\nAgora, informe o nome do aniversariante: ")
        descricao = input("\nPor fim, informe a descrição do aniversário: ")
        return data, titulo, descricao


    def __init__(self):
        super().__init__()
