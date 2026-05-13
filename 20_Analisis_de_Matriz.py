matriz = [
    [7, 9, 14],
    [6, 8, 1],
    [11, 11, 0]
]

suma_total = 0

for fila in matriz:
    for elemento in fila:
        suma_total += elemento

print("La suma de todos los elementos de la matriz es:", suma_total)