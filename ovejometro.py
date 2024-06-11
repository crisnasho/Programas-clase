"""
Un ovejero que cuenta ovejas con forma de oveja y que tienen lana de oveja
necesita un programa para determinar el precio de las ovejas con lana de oveja.

Para eso le pide crear un programa que determine el precio segun los siguientes atributos de una oveja:

Color, Peso, Tamaño

"""

peso_oveja = int(input("ingrese peso oveja: "))
color_oveja = str(input("ingrese color oveja: "))
tamano_oveja = int(input("ingrese tamaño oveja: "))

precio_base = 0

if peso_oveja >= 60: #si el peso de la oveja es igual o mayor a 60
    precio_peso = precio_base + 1500 #al precio base se le suma 1500
else: #si es menor a 60
    precio_peso = precio_base + 1000 #se le suma solo 1000

if color_oveja == "negro": #si el color de la oveja es negro
    precio_color = precio_base + 100 #se le suman 100
elif color_oveja == "morado": #pero si es morado
    precio_color = precio_base + 200 #se le suma 200
elif color_oveja == "ocre": #y si es ocre
    precio_color = precio_base + 150 #se le suma 150

if tamano_oveja == 60: #si el tamaño de la oveja es igual a 60
    precio_tamaño = print(precio_base + 300) #se le suma 300
elif tamano_oveja > 100: #pero si es mayor a 100
    precio_tamano = print(precio_base + 1000) #se le suma 1000
#hay que sumar todos los atributos para tener el precio final

print("el precio de la oveja según los atributos es: ")