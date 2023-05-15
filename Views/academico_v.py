from Views.evento_v import EventoV


def bar():
    print("=" * 32)


class AcademicoV(EventoV):
    def __init__(self):
        super().__init__()

    def mensagem(self, message: str):
        print(message)

    def capturar(self, message) -> str:
        while True:
            try:
                escolha = int(input(message))
            except ValueError:
                self.mensagem("Erro: A opção escolhida deve ser um número"
                              " inteiro.")
            else:
                break
        return escolha

    def mostrar_data(self, data):
        print("\nData: ", data)

    def mostrar_titulo(self, titulo):
        print("\nTítulo: ", titulo)

    def mostrar_descricao(self, descricao):
        print("\nDescrição: ", descricao)

    def mostrar_materia(self, materia):
        print("\nMatéria: ", materia)

    def mostrar_professor(self, professor):
        print("\nProfessor: ", professor)

    def mostrar_tudo(self, academico):
        print("Título: ", academico.titulo)
        print("Data: ", academico.data[0:2], "/", academico.data[2:])
        print("Matéria: ", academico.materia)
        print("Professor: ", academico.professor)
        print("Detalhes: ", academico.descricao)

    def incluir_evento(self) -> tuple:
        while True:
            dia = input("\nInforme o dia: ").zfill(2)
            if not dia.isdigit() or int(dia) < 1 or int(dia) > 31:
                print("\nError: Dia inválido!Tente novamente")
            else:
                break
        while True:
            mes = input("\nAgora, informe o mês: ").zfill(2)
            if not mes.isdigit() or int(mes) < 1 or int(mes) > 12:
                print("\nError: Mês inválido!Tente novamente")
            else:
                break
        data = dia + mes
        titulo = input("\nInforme o tipo de atividade: ")
        materia = input("\nInforme a matéria: ")
        professor = input("\nInforme o(a) professor(a): ")
        descricao = input("\nPor fim, informe a descrição: ")
        return data, titulo, materia, professor, descricao

    def alterar_evento(self) -> tuple:
        titulo = input("\nInforme o novo tipo de atividade: ")
        materia = input("\nInforme a nova matéria: ")
        professor = input("\nInforme o(a) novo(a) professor(a): ")
        descricao = input("\nPor fim, informe a nova descrição: ")
        return titulo, materia, professor, descricao

    def menu(self, chave: str) -> int:
        bar()
        print("MENU EVENTOS ACADÊMICOS DIA: ", chave[0:2], "/", chave[2:])
        bar()
        opcoes = ("1 - Visualizar eventos acadêmicos", "2 - Editar eventos"
                  " acadêmicos", "3 - Excluir eventos acadêmicos",
                  "0 - Voltar ao menu do calendário")
        for opcao in opcoes:
            print(opcao)
        return self.capturar("Selecione uma das opções: ")
