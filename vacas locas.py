nom_cow = [ "Juan Daniel", "Achraf", "Jessica", "Bernardo", "Rosario", "Alexis", "Ariana",
"Sacramento", "Patrocinio", "Patroclo", "Viviana", "Aroa", "Remedios", "Luis",
"David", "Urko", "Rosa", "Isabel", "Gael", "Josep", "Oriol", "Maria", "Josefa", "Elsa"]

lista_cow = []
letra = str(input("ingrese letra: ")).lower()

for nombre in nom_cow:
    if letra in nombre.lower():
        lista_cow.append(nombre)
for contador, vaquitas in enumerate(lista_cow, start = 1):
    print(contador, vaquitas)

num_cow = int(input('seleccione vaca: '))
num_cow -=1
print('Nombre de la vaca seleccionada >', lista_cow[num_cow])