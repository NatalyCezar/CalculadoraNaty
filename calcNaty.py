import PySimpleGUI as sg
from math import factorial

def calcular_fatorial(n):
    try:
        result = factorial(int(n))
        return str(result)
    except ValueError:
        return "Erro"

def calcular_tabuada(n):
    try:
        n = int(n)
        tabuada = "\n".join([f"{n} x {i} = {n * i}" for i in range(0, 11)])
        return tabuada
    except ValueError:
        return "Erro"

layout = [
    [sg.Text("Número:"), sg.InputText(key='-NUM-')],
    [sg.Radio('Fatorial', 'RADIO1', key='-FATORIAL-', default=True),
     sg.Radio('Tabuada', 'RADIO1', key='-TABUADA-')],
    [sg.Button('Calcular')],
    [sg.Text('', size=(20, 11), key='-RESULT-')],
]

window = sg.Window('Calculadora', layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Calcular':
        num = values['-NUM-']

        if values['-FATORIAL-']:
            resultado = calcular_fatorial(num)
        else:
            resultado = calcular_tabuada(num)

        window['-RESULT-'].update(resultado)

window.close()


