import PySimpleGUI as sg


class CalendarioV2:
    def __init__(self):
        self.__window = None
        self.__window_tipo = None
        self.__window_data = None
        self.init_components()

    @property
    def window(self):
        return self.__window

    @property
    def window_tipo(self):
        return self.__window_tipo

    @property
    def window_data(self):
        return self.__window_data

    def init_components(self):
        sg.SetOptions(background_color='#061D49',
                      text_element_background_color='#061D49',
                      element_background_color='#061D49',
                      scrollbar_color=None,
                      input_elements_background_color='#D9D9D9',
                      button_color=('#061D49', '#8CD1DC'),
                      font=('Verdana', 12))
        layout_esquerda = [
            [sg.Image(filename="calendario.png")]
        ]
        sz = (40, 2)
        layout_direita = [
                    [sg.Button('Incluir/editar evento',
                               size=sz, key='-IE-')],
                    [sg.Button('Visualizar eventos',
                               size=sz, key='-VW-')],
                    [sg.Button('Deletar Calandário',
                               size=sz, key='-DEL-')],
                    [sg.Button('Voltar ao menu inicial',
                               size=sz, key='-HOME-')],
                ]

        layout_principal = [
            [sg.Column(layout_esquerda),
             sg.VSeparator(),
             sg.Column(layout_direita)]
        ]

        layout_tipo = [
            [sg.Text('Escolha o tipo de evento')],
            [sg.Radio('Aniversário', 'grupo_1', default=True, key='1')],
            [sg.Radio('Social', 'grupo_1', key='2')],
            [sg.Radio('Academico', 'grupo_1', key='3')],
            [sg.Submit('Prosseguir')]
        ]

        layout_data = [
            [sg.Text('Dia:'), sg.InputCombo((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                            12, 13, 14, 15, 16, 17, 18, 19, 20,
                                            21, 22, 23, 24, 25, 26, 27, 28, 29,
                                            30, 31))],
            [sg.Text('Mês:'), sg.InputCombo((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                            12))],
            [sg.Submit('Prosseguir')]
        ]

        self.__window = sg.Window('Oniverso', layout_principal)
        self.__window_tipo = sg.Window('Oniverso', layout_tipo)
        self.__window_data = sg.Window('Oniverso', layout_data)

    def mensagem(self, texto: str):
        sg.Popup(texto)

    def capturar(self, texto: str) -> str:
        return sg.popup_get_text(texto)

    def menu_calendario(self):
        self.init_components()
        return self.__window.read()

    def tipo_evento(self):
        self.init_components()
        event, values = self.__window_tipo.read()
        if event == 'Prosseguir':
            return values

    def puxar_data(self):
        self.init_components()
        event, values = self.__window_data.read()
        if event == 'Prosseguir':
            data = ''
            for dupla in values.items():
                data += str(dupla[1]).zfill(2)
            return data
