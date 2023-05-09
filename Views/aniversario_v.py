from Views.evento_v import EventoV


def bar():
    print("=" * 32)


class AniversarioV(EventoV):
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

    def mostrar_data(self, data):
        print("\nData: ", data)

    def mostrar_titulo(self, titulo):
        print("\nTítulo: ", titulo)

    def mostrar_descricao(self, descricao):
        print("\nDescrição: ", descricao)

    def mostrar_tudo(self, aniversario):
        print("Aniversariante: ", aniversario.titulo)
        print("Data: ", aniversario.data[0:2], "/", aniversario.data[2:])
        print("Detalhes: ", aniversario.descricao)

    def incluir_evento(self) -> tuple:
        dia = input("\nInforme o dia do aniversário: ").zfill(2)
        mes = input("\nAgora, informe o mês do aniversário: ").zfill(2)
        data = dia + mes
        titulo = input("\nAgora, informe o(s) nome(s) do(s) aniversariante(s): ")
        descricao = input("\nPor fim, informe a descrição do(s) aniversário(s): ")
        return data, titulo, descricao

    def alterar_evento(self) -> tuple:
        titulo = input("\nInforme o(s) novo(s) nome(s) do(s) aniversariante(s): ")
        descricao = input("\nPor fim, informe a nova descrição do(s) aniversário(s): ")
        return titulo, descricao

    def menu(self, chave: str) -> int:
        bar()
        print("MENU ANIVERSÁRIOS DIA: ", chave[0:2], "/", chave[2:])
        bar()
        opcoes = ("1 - Visualizar aniversários", "2 - Editar aniversários", "3 - Excluir aniversários",
                  "0 - Voltar ao menu do calendário")
        for opcao in opcoes:
            print(opcao)
        return self.capturar("Selecione uma das opções: ")

    def __init__(self):
        super().__init__()
