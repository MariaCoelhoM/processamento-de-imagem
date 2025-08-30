# Importing Image from PIL package 
from PIL import Image

# creating a image object
from PIL import Image 

variavel = Image.open("Mcdonalds.jpg")
px = variavel.load()

print(variavel.size) 
width, height = variavel.size
print(width)
print(height)
#print(variavel.filename)
#print(variavel.format)
#print(variavel.format_description)
print (px[4, 4])
px[4, 4] = (0, 0, 0)
print (px[4, 4])
coordinate = x, y = 180, 79

# using getpixel method
print (variavel.getpixel(coordinate))