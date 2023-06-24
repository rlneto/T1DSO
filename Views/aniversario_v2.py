from Views.evento_v2 import EventoV2
import PySimpleGUI as sg


class AniversarioV2(EventoV2):
    def __init__(self):
        super().__init__()
        self.__window = None
        self.__window_tabela = None

    @property
    def window(self):
        return self.__window

    @property
    def window_tabela(self):
        return self.__window_tabela

    def init_components(self, aniversario, data):
        sg.SetOptions(background_color='#061D49',
                      text_element_background_color='#061D49',
                      element_background_color='#061D49',
                      scrollbar_color=None,
                      input_elements_background_color='#D9D9D9',
                      button_color=('#061D49', '#8CD1DC'),
                      font=('Verdana', 12))

        layout_tabela = [[]]
        if data == 32:
            layout_tabela = [
                [sg.Table(values=aniversario, headings=['Data',
                                                        'aniversariante',
                                                        'Descrição'],
                          justification='left',
                          auto_size_columns=False,
                          col_widths=[10, 50, 50],
                          display_row_numbers=True,
                          num_rows=10,
                          key='-TABLE-')],
                [sg.Button('Voltar')]
            ]

        layout_esquerda = [
            [sg.Image(filename='aniversario.png')]
        ]
        layout_direita = [[]]
        if aniversario is None and data != 32:
            layout_direita = [
                [sg.Text(f'Data: {data[:2]}/{data[-2:]}')],
                [sg.Text('Nome(s):'), sg.Push(), sg.InputText()],
                [sg.Text('Descrição:'), sg.Push(), sg.InputText()],
                [sg.Submit('Salvar'), sg.Push(), sg.Button('Voltar')]
            ]
        elif data != 32:
            layout_direita = [
             [sg.Text(f"Data: {data[:2]}/{data[-2:]}")],
             [sg.Text("Nome(s):"), sg.Push(),
              sg.InputText(aniversario.titulo)],
             [sg.Text("Descrição:"), sg.Push(),
              sg.InputText(aniversario.descricao)],
             [sg.Submit('Salvar'), sg.Push(), sg.Button('Voltar')]
            ]

        layout_principal = [
            [sg.Column(layout_esquerda),
             sg.VSeparator(),
             sg.Column(layout_direita)]
        ]

        self.__window = sg.Window('Oniverso', layout_principal)
        self.__window_tabela = sg.Window('Oniverso', layout_tabela)

    def mensagem(self, texto: str):
        sg.Popup(texto)

    def capturar(self, texto: str):
        while True:
            janela = sg.Window(texto, [[sg.InputText(default_text='', key='-TEXTO-')],
                                       [sg.Button('OK'), sg.Button('Cancelar')]])
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

    def listar(self, dados):
        self.init_components(dados, 32)
        event, values = self.__window_tabela.read()
        if event == "Voltar":
            self.__window_tabela.close()
            return True

    def mostrar_e_incluir(self, aniversario, data):
        self.init_components(aniversario, data)
        event, values = self.__window.read()
        if event == "Salvar":
            self.__window.close()
            dados = [data]
            for dupla in values.items():
                dados.append(dupla[1])
            print(dados)
            return dados
        else:
            self.__window.close()
            return "-HOME-"
