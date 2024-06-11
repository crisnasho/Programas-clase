"""
Recolectar las frutas y anotarlas x tipo
y el peso (kg) en dos listas cada cosa
1ra tipos de frutas recolectadas
2da peso de las futas
"""
f = str(input(">> "))
p = str(input(">>> "))
frutas = ['manzana', 'tomate', 'limon', 'sandia', 'naranja']
kilos = [0.5, 1, 1.2, 1.5, 2, 2.2]

i = 0
venta_total = 0
while len(frutas) > 0:
    
    if i >= len(frutas):
        break

    tipo_fruta = frutas[i]

    if tipo_fruta == 'manzana':
        venta_total += kilos[i] * 1500
    
    if tipo_fruta == 'tomate':
        venta_total += kilos[i] * 3000
    
    if tipo_fruta == 'limon':
        venta_total += kilos[i] * 700

    if tipo_fruta == 'sandia':
        venta_total += kilos[i] * 7000
    
    if tipo_fruta == 'naranja':
        venta_total += kilos[i] * 800
    
    i += 1

print("la venta es: ")
print("$",venta_total)