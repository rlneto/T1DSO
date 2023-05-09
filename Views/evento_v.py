from abc import ABC, abstractmethod


class EventoV(ABC):
    @abstractmethod
    def mostrar_data(self, data):
        print("\nData: ", data)


    @abstractmethod
    def mostrar_titulo(self, titulo):
        print("\nTítulo: ", titulo)


    @abstractmethod
    def mostrar_descricao(self, descricao):
        print("\nDescrição: ", descricao)


    @abstractmethod
    def incluir_evento(self) -> tuple:
        dia = input("\nInforme o dia do evento: ")
        mes = input("\nAgora, informe o mês do evento: ")
        data = dia+mes
        dia, mes = None, None
        titulo = input("\nAgora, informe o titulo do evento: ")
        descricao = input("\nPor fim, informe a descrição do evento: ")
        return data, titulo, descricao

    @abstractmethod
    def mensagem(self, message: str):
        pass

    @abstractmethod
    def capturar(self, message) ->str:
        pass

    @abstractmethod
    def alterar_evento(self) ->tuple:
        pass

    @abstractmethod
    def menu(self) ->int:
        pass


    def __init__(self):
        pass
