import PySimpleGUI as sg


class CalendarioV2:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('Dark')
        tipos_evento = ("Social", "Acadêmico", "Aniversário")
        layout = [[sg.Text('Opções do calendário')],
                  [sg.Radio('Incluir/editar evento', 'grupo_2', key='-IE-'),
                   sg.Combo(tipos_evento, default_value="Aniversário" ,k='-TIPO-')],
                  [sg.CalendarButton('Escolher data', key='-DATA-')],
                  [sg.Radio('Visualizar eventos', 'grupo_2', default=True, key='-VW-'),
                   sg.Check('Todos os eventos?', key='-ALL-')],
                  [sg.Radio('Excluir Calendário', 'grupo_2', key='-DEL-'), sg.Text('Senha de Admin: '),
                   sg.InputText('', size=(3, 1), key='-ADM-')],
                  [sg.Submit('Voltar'), sg.Submit('Prosseguir')],
                  [[sg.Text('Event: ')], [sg.Text(key='-OUT EVENT-')]],
                  [[sg.Text('Values: ')], [sg.Text(key='-OUT VALUES-')]]
                  ]
        self.__window = sg.Window('Menu do calendário', layout)

    def mensagem(self, texto: str):
        sg.Popup(texto)

    def incluir_evento(self, tipo: str):
        match tipo:
            case "Acadêmico":
                janela = sg.Window('Inclusão de evento acadêmico',
                                 [[sg.Text('Nome do Evento: '), sg.InputText('', key='-TITULO-')],
                                  [sg.Submit('Cancelar'), sg.Submit('Criar Evento')]])
                event, values = janela.read()
                if event == 'Criar Evento':
                    janela.close()
                    return values
                else:
                    janela.close()
            case "Social":
                janela =  sg.Window('Inclusão de evento social',
                                 [[sg.Text('Nome do Evento: '), sg.InputText('', key='-TITULO-')],
                                  [sg.Submit('Cancelar'), sg.Submit('Criar Evento')]])
                event, values = janela.read()
                if event == 'Criar Evento':
                    janela.close()
                    return values
                else:
                    janela.close()
            case "Aniversário":
                janela = sg.Window('Inclusão de Aniversário',
                                 [[sg.Text('Aniversariante: '), sg.InputText('', key='-TITULO-')],
                                  [sg.Submit('Cancelar'), sg.Submit('Criar Evento')]])
                event, values = janela.read()
                janela.close()
                if event == 'Criar Evento':
                    janela.close()
                    return values
                else:
                    janela.close()


    def capturar(self, texto: str) -> str:
        return sg.popup_get_text(texto)

    def menu(self):
        return self.__window.read()

    def update(self):
        self.__window['-OUT EVENT-'].update(event)
        self.__window['-OUT VALUES-'].update(values)

teste = CalendarioV2()
while True:
    event, values = teste.menu()
    if event == 'Cancelar':
        break
    if values['-IE-']:
        values.update(teste.incluir_evento(values['-TIPO-']))
    if event == sg.WIN_CLOSED:
        break
    teste.update()



