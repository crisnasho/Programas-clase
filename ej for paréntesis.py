"""
escribir un programa que reciba un texto hecho solo de
'()'
el programa debe indicar si los parentesis estan bn o no
solo usar 1 for
"""
"(())()"
balanc = 0
"( = +1"
") = -1"
#BIEN

"(()"
bal = 1 #MAL

"((("
bal = 3 #MAL

"(()())"
bal = 0 #BIEN

#SI DA NUM NEGATIVO ESTA MALO

parent = input("ingrese secuencia: ")
contador = 0
secuencia = ''

for secuencia in parent:
    if secuencia == '(':
        contador += 1
    elif secuencia == ')':
        contador -= 1

    if contador != 0 or contador <= -1 or parent[0] == ")":
        secuencia = "no ta god"
    else:
        secuencia = "ta god"
print("la secuencia:",secuencia,"\ncont: ",contador)