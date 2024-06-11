producto = input("ingrese producto que desea comprar: ").lower()
dinero = int(input("ingrese cantidad de dinero disponible: $"))
preproduc = int(input("ingrese el precio del producto: $"))
iva = preproduc*0.19
descuento = 0
pretotal = preproduc + iva
print("el precio total con iva: ",pretotal, ",el iva es del 19%: $", iva)
#---------------------------edad-----------------------------------------
edad = int(input("ingrese su edad: "))
if (edad <= 18) or (edad >= 51 and edad <= 70):
    descuento = 0.05*pretotal
    pretotal = pretotal - descuento
    print("precio correspondiente: ",pretotal, "con el primer descuento: ",descuento)
if edad >= 19 and edad<= 50:
    descuento = 0
    pretotal = pretotal - descuento
    print("precio correspondiente: ",pretotal, "primer descuento: ",descuento)
if edad >= 71:
    descuento = 0.10*pretotal
    pretotal = pretotal - descuento
    print("precio correspondiente: ",pretotal, "primer descuento: ",descuento)
#-------------------------------met pago------------------------------------------
metpago = input("ingrese metodo de pago(debito/credito/efectivo/cheque): ").lower()
if metpago == "efectivo":
    descuento = 0
    pretotal = pretotal - descuento
    print("precio correspondiente: ",pretotal, "segundo descuento: ",descuento)
if metpago == "debito":
    descuento = 0.05*pretotal
    pretotal = pretotal - descuento
    print("precio correspondiente: ",pretotal, "segundo descuento: ",descuento)
if metpago == "credito":
    descuento = 0.08*pretotal
    pretotal = pretotal - descuento
    print("precio correspondiente: ",pretotal, "segundo descuento: ",descuento)
if metpago == "cheque":
    descuento = 0.06*pretotal
    pretotal = pretotal - descuento
    print("precio correspondiente: ",pretotal, "segundo descuento: ",descuento)
#-----------------------------precio final----------------------------------------------
if dinero >= pretotal:
    print("el precio final es: ", pretotal, "PUEDE COMPRAR EL PRODUCTO!!!")
else:
    print("el precio final es: ", pretotal, "NO PUEDE COMPRAR EL PRODUCTO!!!")