import PySimpleGUI as sg


class CalendarioV2:
    def __init__(self):
        self.__window = None
        self.__window_tipo = None
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
            [sg.Image(filename="calendario.png")]
        ]
        sz = (40, 2)
        layout_direita = [
                    [sg.Button('Incluir/editar evento',
                               size=sz, key='-IE-')],
                    [sg.Button('Visualizar eventos',
                               size=sz, key='-VW-')],
                    [sg.Button('Voltar ao menu inicial',
                               size=sz, key='-HOME-')]
                ]

        layout_principal = [
            [sg.Column(layout_esquerda),
             sg.VSeparator(),
             sg.Column(layout_direita)]
        ]

        layout_tipo = [
            [sg.Text('Escolha o tipo de evento')],
            [sg.Radio('Aniversário','grupo_1', default=True, key='1')],
            [sg.Radio('Social', 'grupo_1', key='2')],
            [sg.Radio('Academico', 'grupo_1', key='3')],
            [sg.Submit('Prosseguir')]
        ]

        # layout = [[sg.Text('Opções do calendário')],
        #           [sg.Radio('Incluir/editar evento', 'grupo_2', key='-IE-'), sg.Text('Dia: '),
        #            sg.InputText('', key='-DIA-'), sg.Text('Mês: '), sg.InputText('', key='-MES-')],
        #           [sg.Radio('Visualizar eventos', 'grupo_2', default=True, key='-VW-')],
        #           [sg.Radio('Voltar ao menu inicial', 'grupo_2', key='-HOME-')],
        #           [sg.Radio('Excluir Calendário', 'grupo_2', default=True, key='-DEL-'), sg.Text('Senha de Admin: '),
        #            sg.InputText('', key='-ADM-')],
        #           [sg.Submit('Prosseguir')]]
        self.__window = sg.Window('Oniverso', layout_principal)
        self.__window_tipo = sg.Window('Oniverso', layout_tipo)

    def mensagem(self, texto: str):
        sg.Popup(texto)

    def capturar(self, texto: str) -> str:
        return sg.popup_get_text(texto)

    def menu_calendario(self):
        return self.__window.read()

    def tipo_evento(self, verbo):
        event, values = self.__window_tipo.read()
        if event == 'Prosseguir':
            return values