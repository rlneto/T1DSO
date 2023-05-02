def bar():
    print("=" * 20)


class SistemaV:
    def mensagem(self, message: str):
        print(message)

    def capturar(self, message) -> str:
        return input(message)

    def __init__(self):
        pass

    def menu(self) -> str:
        bar()
        print("      ONIVERSO      ")
        bar()
        opcoes = ("1 - Criar Calendário", "2 - Acessar Calendário", "9 - Visualizar Calendários (Admin)", "0 - Sair")
        for opcao in opcoes:
            print(opcao)
        return self.capturar("Selecione uma opção: ")
