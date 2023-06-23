import PySimpleGUI as sg

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

# Lista de objetos Person
people = [
    Person('John', 25, 'New York'),
    Person('Jane', 30, 'London'),
    Person('Bob', 40, 'Paris')
]

# Converter objetos em listas de valores
data = [[person.name, person.age, person.city] for person in people]

# Definir a estrutura da tabela
layout = [
    [sg.Table(values=data, headings=['Name', 'Age', 'City'],
              justification='left',
              display_row_numbers=True,
              num_rows=10,
              key='-TABLE-')],
    [sg.Button('Fechar')]
]

# Criar a janela
window = sg.Window('Tabela', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Fechar':
        break

window.close()

