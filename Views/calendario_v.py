def bar():
    print("=" * 25)


class CalendarioV:
    def __init__(self):
        pass

    def mensagem(self, message: str):
        print(message)

    def capturar(self, message) -> int:
        while True:
            try:
                escolha = int(input(message))
            except ValueError:
                self.mensagem("Erro: A opção escolhida deve ser um número"
                              " inteiro.")
            else:
                break
        return escolha

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
        opcoes = ("\n1 - Incluir/editar Evento",  "2 - Visualizar Eventos",
                  "3 - Acessar Evento por dia",
                  "0 - Voltar ao menu do sistema")
        for item in opcoes:
            print(item)
        return self.capturar("\nSelecione uma das opções: ")

    def puxar_data(self) -> str:
        while True:
            dia = input("Informe o dia: ").zfill(2)
            if not dia.isdigit() or int(dia) < 1 or int(dia) > 31:
                print("\nError: Dia inválido!Tente novamente")
            else:
                break
        while True:
            mes = input("Agora, informe o mês: ").zfill(2)
            if not mes.isdigit() or int(mes) < 1 or int(mes) > 12:
                print("\nError: Mês inválido!Tente novamente")
            else:
                break
        return dia + mes
