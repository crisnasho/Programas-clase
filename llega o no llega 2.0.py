distancia = int(input("Ingrese distancia: "))

print(distancia, metro, micro) #debugear las variables para ver errores

if(distancia < 500):
    print("si llega")
else: # distancia mayor 500
    if(distancia <= 1500):
        if(metro or micro):
            print("si llega")
        else:
            print("no llega")
    else: #mayor a 500
        if(metro and micro):
            print("si llega")
        else:
            print("no llega")