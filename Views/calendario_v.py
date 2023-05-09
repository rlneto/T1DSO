def bar():
    print("=" * 25)


class CalendarioV:
    def mensagem(self, message: str):
        print(message)

    def capturar(self, message) -> str:
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

    def listagem(self, frase: str):
        print("Calendário encontrado!")
        print("Chave: ", frase)

    def sucesso(self, chave: str):
        print("Calendário criado com sucesso.\nChave: {}".format(chave))

    def tipo_evento(self, verbo):
        print("Escolha o tipo de Evento para", verbo)
        opcoes = ("\n1 - Aniversáio",  "2 - Social", "3 - Academico",
                  "0 - Voltar às opções do calendário")
        for item in opcoes:
            print(item)
        return self.capturar("\nSelecione uma das opções: ")


    def menu_calendario(self, chave: str) -> int:
        bar()
        print("OPÇÕES DO CALENDÁRIO: {}".format(chave))
        bar()
        opcoes = ("\n1 - Incluir Evento",  "2 - Visualizar Eventos", "3 - Acessar Evento por dia",
                  "0 - Voltar ao menu do sistema")
        for item in opcoes:
            print(item)
        return self.capturar("\nSelecione uma das opções: ")

    def puxar_data(self) -> str:
        dia = input("Informe a o dia do Aniversário: ").zfill(2)
        mes = input("Agora, informe o mês do Aniversário: ").zfill(2)
        return dia + mes
