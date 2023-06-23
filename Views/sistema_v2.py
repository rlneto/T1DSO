import PySimpleGUI as sg


class SistemaV2:
    def __init__(self):
        self.__window = None
        self.init_components()

    @property
    def window(self):
        return self.__window
    def init_components(self):
        sg.SetOptions(background_color='#061D49',
                      text_element_background_color='#061D49',
                      element_background_color='#061D49',
                      scrollbar_color=None,
                      input_elements_background_color='#D9D9D9',
                      button_color=('#061D49', '#8CD1DC'),
                      font=('Verdana', 12))
        layout_esquerda = [
            [sg.Image(filename="inicio.png")]
        ]
        sz = (40, 2)
        layout_direita = [
                    [sg.Button('Criar calendário',
                               size=sz, key='-CC-')],
                    [sg.Button('Acessar calendário',
                               size=sz, key='-AC-')],
                    [sg.Button('Menu de desenvolvedor',
                               size=sz, key='-DEV-')]
                ]

        layout = [
            [sg.Column(layout_esquerda),
             sg.VSeparator(),
             sg.Column(layout_direita)]
        ]
        self.__window = sg.Window('ONIVERSO', layout)

    def mensagem(self, texto: str):
        sg.Popup(texto)

    def capturar(self, texto: str) -> str:
        return sg.popup_get_text(texto)

    def menu(self):
        self.init_components()
        return self.__window.read()
