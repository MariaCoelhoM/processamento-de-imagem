from PIL import Image 

variavel = Image.open("Mcdonalds.jpg")
variavel.show("mcdonald's")

print(variavel.size) 
width, height = variavel.size
print(width)
print(height)
print(variavel.filename)
print(variavel.format)
print(variavel.format_description)
