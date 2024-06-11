velocidad_auto = int(input("ingrese velocidad: "))
velocidad_limite = int(input("ingrese velocidad limite: "))
exceso = ((velocidad_auto - velocidad_limite) / velocidad_limite) * 100 

if velocidad_auto > velocidad_limite:
    print("excede el limite de velocidad compare!!!")
    if velocidad_auto > velocidad_limite:
        print(exceso, "%")

if exceso == 0:
    print("no excede el limite mi rey")
    if exceso > 0 and exceso <= 15:
        multa1 = 10*velocidad_auto
        print("tiene una multa de: $", multa1)
    else:
        if exceso >= 16 and exceso <= 25:
            multa2 = 40*velocidad_auto
            print("tiene una multa de: $", multa2)
        else:
            if exceso >= 26 and exceso <= 50:
                multa3 = 4000 + (15*velocidad_auto)
                print("tiene una multa de: $", multa3)
            else:
                if exceso >= 51:
                    multa4 = 10000+(30*velocidad_auto)
                    print("tiene una multa de: $", multa4)