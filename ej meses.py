"""
crea un programa que pida un número al usuario un núm del mes
(ej, 4) y diga cuantos días tiene (ej, 30) y el nombre del mes. Debes usar un par
de listas. Para simplificarlo vamos a suponer que feb tiene 28 días.
"""
nombre = ['enero', 'febrero', 'marzo', 'abril', 'mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
dias = [31,28,31,30,31,30,31,31,30,31,30,31]

mes = int(input("ingrese num: "))
mes -= 1
print(nombre[mes], dias[mes])