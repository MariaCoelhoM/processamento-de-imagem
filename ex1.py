import FreeSimpleGUI as sg

layout = [
    [sg.Text("Bem vindo Maria Eduarda :")],
    [sg.InputText(key = "-INPUT-")],
    [sg.Button("Mostrar valor!")]
]

window = sg.Window("Botões", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Mostrar valor!":
        input_text = values["-INPUT-"]
        sg.popup(f"Você digitou: {input_text}")

window.close()