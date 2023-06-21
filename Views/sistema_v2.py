import PySimpleGUI as sg


class SistemaV2:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('Dark')
        layout = [[sg.Text('ONIVERSO')],
                  [sg.Radio('Criar calendário', 'grupo_1', key='-CC-')],
                  [sg.Radio('Acessar calendário', 'grupo_1', default=True, key='-AC-'), sg.Text('Chave: '),
                   sg.InputText('', key='-KEY-')],
                  [sg.Radio('Menu de desenvolvedor', 'grupo_1', key='-DEV-')],
                  [sg.Submit('Prosseguir')]]
        self.__window = sg.Window('Oniverso', layout)

    def mensagem(self, texto: str):
        sg.Popup(texto)

    def capturar(self, texto: str) -> str:
        return sg.popup_get_text(texto)

    def menu(self):
        return self.__window.read()
