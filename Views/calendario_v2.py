import PySimpleGUI as sg


class CalendarioV2:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('Dark')
        layout = [[sg.Text('Opções do calendário')],
                  [sg.Radio('Incluir/editar evento', 'grupo_2', key='-IE-'), sg.Text('Dia: '),
                   sg.InputText('', key='-DIA-'), sg.Text('Mês: '), sg.InputText('', key='-MES-')],
                  [sg.Radio('Visualizar eventos', 'grupo_2', default=True, key='-VW-')],
                  [sg.Radio('Voltar ao menu inicial', 'grupo_2', key='-HOME-')],
                  [sg.Radio('Excluir Calendário', 'grupo_2', default=True, key='-DEL-'), sg.Text('Senha de Admin: '),
                   sg.InputText('', key='-ADM-')],
                  [sg.Submit('Prosseguir')]]
        self.__window = sg.Window('Oniverso', layout)

