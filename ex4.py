import FreeSimpleGUI as sg
from PIL import Image
import io
import PIL.Image
import PIL.ExifTags
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def resize_image(image_path):
    img= Image.open(image_path)
    img= img.resize((800,600), Image.Resampling.LANCZOS)
    return img

def get_exif(image_file_path):
    exif_table = {}
    image = Image.open(image_file_path)
    info = image.getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_table[decoded] = value
    return exif_table

def get_gps(image_file_path):
    gps_table = {}
    exif_table = {}

    image = Image.open(image_file_path)
    info = image.getexif()
    
    GPSINFO_TAG = next(
        tag for tag, name in TAGS.items() if name == "GPSInfo"
    ) 
    gpsinfo = info.get_ifd(GPSINFO_TAG)

    print(gpsinfo)
    north = gpsinfo[2]
    east = gpsinfo[4]

    lat = ((float(north[0]) * 60 + float(north[1])) * 60 + float(north[2])) / 3600
    lon = -((float(east[0]) * 60 + float(east[1])) * 60 + float(east[2])) / 3600 
    print(lat)
    print(lon)
    

    return gps_table


layout = [
    [sg.Menu([["Arquivo",["Abrir", "Fechar"]],["EXIF",["Mostrar dados da imagem","Mostrar dados do GPS"]],["Sobre a imagem",["Tamanho MB", "Descrição" ,"Formato"]],["Sobre",["Aluno"]]])],
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
            
            resized_img =resize_image(file_path)
            #Converte a imagem PIL para o formato que o PySimpleGUI
            img_bytes =io.BytesIO()# Permite criar objetos semelhantes a arquivos na memoria
            resized_img.save(img_bytes, format="PNG")
            window["-IMAGE-"].update(data=img_bytes.getvalue())
    
    
    elif event == "Aluno":
        sg.popup("Desenvolvido pelo BCC - 6 semestre. \n\n Maria Eduarda Mariano Coelho")
    elif event == "Mostrar dados da imagem":
        sg.popup("teste")
        #dicio = get_exif(file_path)
        #sg.popup(dicio{0x01,})
    elif event == "Mostrar dados do GPS":
        sg.popup(get_gps(file_path))

window.close()