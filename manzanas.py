peso = int(input("ingrese peso de la manzana: "))
radio = int(input("ingrese radio de la manzana: "))
densidad = int(input("ingrese densidad de la manzana: "))
gusanos = int(input("ingrese cantidad de gusanos: "))

manzana_ver = "no se puede recoger aun" 
manzana_roj = "no se puede recoger aun"
manzana_mor = "no se puede recoger aun"
manzana_azu = "no se puede recoger aun"

if peso >= 12 and densidad == 15 and gusanos == 0:
    manzana_ver = "se puede recoger la manzana verde"
    print(manzana_ver)
elif peso >1 and radio == 13 and densidad >= 10 and gusanos == 0:
    manzana_roj = "se puede recoger la manzana roja"
    print(manzana_roj)
elif peso <= 14 and radio == 16 and densidad >= 12 and gusanos == 0:
    manzana_mor = "puede recoger la manzana morada"
    print(manzana_mor)
elif peso == 13 and radio != 10 and gusanos == 1:
    manzana_azu = "puede recoger la manzana azul"
    print(manzana_azu)
else:
    print("no puede recoger ninguna manzana")