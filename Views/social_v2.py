from Views.evento_v2 import EventoV2
import PySimpleGUI as sg


class socialV2(EventoV2):
    def __init__(self):
        super().__init__()
        self.__window = None

    @property
    def window(self):
        return self.__window

    def init_components(self, social, data):
        sg.SetOptions(background_color='#061D49',
                      text_element_background_color='#061D49',
                      element_background_color='#061D49',
                      scrollbar_color=None,
                      input_elements_background_color='#D9D9D9',
                      button_color=('#061D49', '#8CD1DC'),
                      font=('Verdana', 12))
        layout_esquerda = [
            [sg.Image(filename='social.png')]
        ]
        if social is None:
            layout_direita = [
                [sg.Text(f'Data: {data[:2]}/{data[-2:]}')],
                [sg.Text('Título:'), sg.InputText()],
                [sg.Text('Local:'), sg.InputText()],
                [sg.Text('Descrição:'), sg.InputText()]
                [sg.Submit('Salvar'), sg.Button('Voltar')]
            ]
        else:
            layout_direita = [
             [sg.Text(f"Data: {data[:2]}/{data[-2:]}")],
             [sg.Text("Título:"), sg.InputText(social.titulo)],
             [sg.Text("Local:"), sg.InputText(social.local)],
             [sg.Text("Descrição:"), sg.InputText(social.descricao)],
             [sg.Submit('Salvar'), sg.Button('Voltar')]
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

    def mostrar_e_incluir(self, social, data):
        self.init_components(social, data)
        event, values = self.__window.read()
        if event == "Salvar":
            dados = [data]
            for dupla in values.items():
                dados.append(dupla[1])
            print(dados)
            return dados
        else:
            return "-HOME-"
