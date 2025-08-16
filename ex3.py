import FreeSimpleGUI as sg

layout = [
    [sg.Menu([["Arquivo",["Abrir", "Fechar"]],["Ajuda",["Sobre"]]])],
    [sg.Image(key ="-IMAGE-", size=(800,600))],
]

window = sg.Window("Menu a Get File", layout, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Fechar":
        break
    elif event == "Abrir":
        file_path = sg.popup_get_file("Selecionar uma imagem", file_types=(("Imagens","*.jpg *.png"),))
        if file_path:
            window["-IMAGE-"].update(filename=file_path)
    elif event == "Sobre":
        sg.popup("Desenvolvido pelo BCC - 6 semestre. \n\n Maria Eduarda Mariano Coelho")

window.close()