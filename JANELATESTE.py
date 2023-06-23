import PySimpleGUI as sg

sg.SetOptions(background_color='#061D49',
              text_element_background_color='#061D49',
              element_background_color='#061D49',
              scrollbar_color=None,
              input_elements_background_color='#D9D9D9',
              button_color=('#061D49', '#8CD1DC'))

layout_esquerda = [
    [sg.Image(filename="inicio.png")]
]
layout_direita = [
            [sg.Button('Criar calendário', size=(50, 2))],
            [sg.Button('Acessar calendário', size=(50, 2))],
            [sg.Button('Menu de desenvolvedor', size=(50, 2))]
        ]

layout = [
    [sg.Column(layout_esquerda),
     sg.VSeparator(),
     sg.Column(layout_direita)]
]
window = sg.Window('Oniverso', layout)
window.read()
