from Views.evento_v import EventoV


def bar():
    print("=" * 32)


class SocialV(EventoV):
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

    def mostrar_local(self, local):
        print("\nLocal: ", local)

    def mostrar_tudo(self, socical):
        print("Título: ", socical.titulo)
        print("Data: ", socical.data[0:2], "/", socical.data[2:])
        print("Local: ", socical.local)
        print("Detalhes: ", socical.descricao)

    def incluir_evento(self) -> tuple:
        dia = input("\nInforme o dia: ").zfill(2)
        mes = input("\nAgora, informe o mês: ").zfill(2)
        data = dia + mes
        titulo = input("\nInforme o tipo de atividade: ")
        local = input("\nInforme o local: ")
        descricao = input("\nPor fim, informe a descrição: ")
        return data, titulo, local, descricao

    def alterar_evento(self) -> tuple:
        titulo = input("\nInforme o novo tipo de atividade: ")
        local = input("\nInforme o novo local: ")
        descricao = input("\nPor fim, informe a nova descrição: ")
        return titulo, local, descricao

    def menu(self, chave: str) -> int:
        bar()
        print("MENU EVENTOS SOCIAIS DIA: ", chave[0:2], "/", chave[2:])
        bar()
        opcoes = ("1 - Visualizar eventos sociais", "2 - Editar eventos sociais", "3 - Excluir eventos sociais",
                  "0 - Voltar ao menu do calendário")
        for opcao in opcoes:
            print(opcao)
        return self.capturar("Selecione uma das opções: ")

    def __init__(self):
        super().__init__()