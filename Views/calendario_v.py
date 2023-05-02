def bar():
    print("=" * 20)


class CalendarioV:
    def __init__(self):
        pass

    def listagem(self, frase: str):
        print("Calendário encontrado!")
        print("Chave: ", frase)

    def sucesso(self, chave: str):
        print("Calendário criado com sucesso.\nChave: {}".format(chave))

    def menu_calendario(self, chave: str) -> str:
        bar()
        print("Opões para o calendário: {}".format(chave))
        opcoes = ("1 - Visualizar Eventos", "2 - Editar Evento")
        return input("\nSelecione uma das opções: ")

    def mensagem(self, message: str):
        print(message)

    def capturar(self, message) -> str:
        return input(message)
