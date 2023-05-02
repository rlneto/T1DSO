def bar():
    print("=" * 25)


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
        print("OPÇÕES DO CALENDÁRIO: {}".format(chave))
        bar()
        opcoes = ("\n1 - Visualizar Aniversários", "2 - Incluir Aniversário", "3 - Editar Aniversário",
                  "4 - Excluir Aniversário", "0 - Voltar ao menu do sistema")
        for item in opcoes:
            print(item)
        return input("\nSelecione uma das opções: ")

    def mensagem(self, message: str):
        print(message)

    def capturar(self, message) -> str:
        return input(message)
