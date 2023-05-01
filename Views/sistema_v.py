def bar():
    print("=" * 20)


class SistemaV:
    def __init__(self):
        pass

    def menu(self):
        bar()
        print("      ONIVERSO      ")
        bar()
        opcoes = ("1 - Criar Calendário", "2 - Acessar Calendário", "0 - Sair")
        for opcao in opcoes:
            print(opcao)
        # print(type(opcoes))
        escolha = input("Selecione uma opção: ")
        return escolha
