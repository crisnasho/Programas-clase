"""
cree un programa que reciba un caracter e indique si es o no es vocal
el programa solo puede recibir 1 caracter a la vez. Si recibe más de uno, debe mostrar "error"
"""

vocal = (input("ingrese solo un caracter: ")).lower()
voc = "a, e, i, o, u"
if(len(vocal))>=2:
    print("ERROR")
elif vocal in voc:
    print("es una vocal")
else:
    print("no es vocal")