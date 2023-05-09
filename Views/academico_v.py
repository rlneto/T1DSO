from Views.evento_v import EventoV


def bar():
    print("=" * 32)


class AcademicoV(EventoV):
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

    def mostrar_materia(self, materia):
        print("\nMatéria: ", materia)

    def mostrar_professor(self, professor):
        print("\nProfessor: ", professor)

    def mostrar_tudo(self, academico):
        print("Título: ", academico.titulo)
        print("Data: ", academico.data[0:2], "/", academico.data[2:])
        print("Matéria: ", academico.materia)
        print("Ptofessor: ", academico.professor)
        print("Detalhes: ", academico.descricao)

    def incluir_evento(self) -> tuple:
        dia = input("\nInforme o dia: ").zfill(2)
        mes = input("\nAgora, informe o mês: ").zfill(2)
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
        opcoes = ("1 - Visualizar eventos acadêmicos", "2 - Editar eventos acadêmicos", "3 - Excluir eventos acadêmicos",
                  "0 - Voltar ao menu do calendário")
        for opcao in opcoes:
            print(opcao)
        return self.capturar("Selecione uma das opções: ")

    def __init__(self):
        super().__init__()