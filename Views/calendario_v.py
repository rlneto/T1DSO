def bar():
    print("=" * 25)


class CalendarioV:
    def mensagem(self, message: str):
        print(message)

    def capturar(self, message) -> str:
        return input(message)

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
        opcoes = ("\n1 - Incluir Aniversário",  "2 - Visualizar Aniversários", "3 - Acessar Aniversário",
                  "0 - Voltar ao menu do sistema")
        for item in opcoes:
            print(item)
        return self.capturar("\nSelecione uma das opções: ")

    def puxar_data(self) -> str:
        dia = input("Informe a o dia do Aniversário: ").zfill(2)
        mes = input("Agora, informe o mês do Aniversário: ").zfill(2)
        return dia + mes
