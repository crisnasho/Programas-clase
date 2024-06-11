distancia_destino = int(input("ingrese distancia: "))
micro = input("hay micro? (si/no)")
metro = input("hay metro? (si/no)")
print(micro = "si")

if distancia_destino <= 500:
    print("puede llegar")
else:
    if(distancia_destino >= 500 or distancia_destino <= 1500):
        print("llega a destino")
        if micro and metro:
            if distancia_destino > 1500:
                print("llega a destino")
                if micro or metro:
                    print()