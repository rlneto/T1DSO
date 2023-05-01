from Controllers.sistema_c import SistemaC


def bar():
    print("="*20)


def menu():
    bar()
    print("      ONIVERSO      ")
    bar()
    opcoes = ("1 - Criar Calendário", )
    for opcao in opcoes:
        print(opcao)
    # print(type(opcoes))


menu()
