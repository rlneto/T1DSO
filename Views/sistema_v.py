

class SistemaV:
    def __init__(self):
        pass

    def bar(self):
        print("=" * 20)

    def menu(self):
        self.bar()
        print("      ONIVERSO      ")
        self.bar()
        opcoes = ("1 - Criar Calendário", "2 - Visualizar Calendário", )
        for opcao in opcoes:
            print(opcao)
        # print(type(opcoes))
        escolha = int(input("Selecione uma opção: "))
        return escolha
