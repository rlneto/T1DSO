def bar():
    print("=" * 20)


class SistemaV:
    def mensagem(self, message: str):
        print(message)

    def capturar(self, message) -> int:
        while True:
            try:
                escolha = int(input(message))
            except ValueError:
                self.mensagem("Erro: A opção escolhida deve ser um número inteiro.")
            else:
                break
        return escolha

    def __init__(self):
        pass

    def menu(self) -> int:
        bar()
        print("      ONIVERSO      ")
        bar()
        opcoes = ("1 - Criar Calendário", "2 - Acessar Calendário", "9 - Visualizar Calendários (Admin)", "0 - Sair")
        for opcao in opcoes:
            print(opcao)
        return self.capturar("Selecione uma opção: ")
