import PySimpleGUI as sg


class SistemaV2:
    def __init__(self):
        self.__window = None
        self.__window_tabela = None
        self.init_components(None)

    @property
    def window(self):
        return self.__window

    @property
    def window_tabela(self):
        return self.__window_tabela

    def init_components(self, dados):
        sg.SetOptions(background_color='#061D49',
                      text_element_background_color='#061D49',
                      element_background_color='#061D49',
                      scrollbar_color=None,
                      input_elements_background_color='#D9D9D9',
                      button_color=('#061D49', '#8CD1DC'),
                      font=('Verdana', 12))
        layout = [[]]
        layout_tabela = [[]]
        if dados is None:
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
                 sg.Column(layout_direita)
                 ]
            ]
        else:
            layout_tabela = [
                [sg.Table(values=dados, headings=['Chave',
                                                  'Senha',
                                                  'Objeto'],
                          justification='left',
                          auto_size_columns=False,
                          col_widths=[5, 5, 60],
                          display_row_numbers=True,
                          num_rows=10,
                          key='-TABLE-')],
                [sg.Button('Voltar')]
            ]
        self.__window = sg.Window('ONIVERSO', layout)
        self.__window_tabela = sg.Window('Oniverso', layout_tabela)

    def mensagem(self, texto: str):
        sg.Popup(texto)

    def capturar(self, texto: str):
        while True:
            janela = sg.Window(texto, [[sg.InputText(default_text='',
                                                     key='-TEXTO-')],
                                           [sg.Button('OK'),
                                            sg.Button('Cancelar')]])
            entrada = janela.read()
            if entrada != 'OK' or sg.WIN_CLOSED:
                janela.close()
                break
            else:
                try:
                    teste = int(entrada[1]['-TEXTO-'])
                except ValueError:
                    sg.Popup('Valor inválido.')
                else:
                    janela.close()
                    break
        return entrada

    def listar_calendarios(self, dados):
        self.init_components(dados)
        retorno = self.__window_tabela.read()
        self.__window_tabela.close()
        return retorno

    def menu(self):
        self.init_components(None)
        return self.__window.read()
