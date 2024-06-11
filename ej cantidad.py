"""
Cree un programa que reciba números enteros (positivos o negativos). El programa deja de recibir números cuando se ingresa 0.
Al final el programa muestra:
La cantidad de números ingresado
El numero mayor
El numero menor
"""
cant = 0
may = 0
men = 0
while (True):
    num = int(input("ingrese num: "))
    if num == 0:
        break

    if cant == 0:
        may = num
        men = num
    
    cant += 1

    if num > may:
        may = num
    
    if num < men:
        men = num

print("cantidad: ",cant)
print("mayor: ",may)
print("menor: ",men)