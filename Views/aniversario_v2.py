from Views.evento_v2 import EventoV2
import PySimpleGUI as sg


class AniversarioV2(EventoV2):
    def __init__(self):
        super().__init__()
        self.__window = None

    def init_components(self, aniversario, data):
        sg.SetOptions(background_color='#061D49',
                      text_element_background_color='#061D49',
                      element_background_color='#061D49',
                      scrollbar_color=None,
                      input_elements_background_color='#D9D9D9',
                      button_color=('#061D49', '#8CD1DC'),
                      font=('Verdana', 12))
        layout_esquerda = [
            [sg.Image(filename='aniversario.png')]
        ]
        if aniversario is None:
            layout_direita = [
                [sg.Text(f'Data: {data[:2]}/{data[-2:]}')],
                [sg.Text('Nome(s):'), sg.InputText()],
                [sg.Text('Descrição:'), sg.InputText()],
                [sg.Submit('Salvar')]
            ]
        else:
            layout_direita = [
            [sg.Text(f"Data: {data[:2]}/{data[-2:]}")],
            [sg.Text("Nome(s):"), sg.InputText(aniversario.titulo)],
            [sg.Text("Descrição:"), sg.InputText(aniversario.descricao)],
            [sg.Submit('Salvar')]
            ]

        layout_principal = [
            [sg.Column(layout_esquerda),
             sg.VSeparator(),
             sg.Column(layout_direita)]
        ]

        self.__window = sg.Window('Oniverso', layout_principal)

    def mensagem(self, texto: str):
        sg.Popup(texto)

    def capturar(self, texto: str) -> str:
        return sg.popup_get_text(texto)

    def incluir_evento(self):
        #print(self.__window.read())
        pass
    
    def mostrar_tudo(self, aniversario, data):
        self.init_components(aniversario, data)
        self.__window.read()
