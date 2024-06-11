amp = "off"
botonA = input("esta encendido A?(si/no): ")
botonB = input("esta encendido B?(si/no): ")
botonC = input("esta encendido C?(si/no): ")

if botonA == "si":
    amp = "prende"

if botonB == "si":
    amp = "prende"

if botonC == "si":
    amp = "no prende"

print("ampolleta", amp)