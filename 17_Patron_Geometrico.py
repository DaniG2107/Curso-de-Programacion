N = int(input("Ingresa la base del triángulo (entero positivo): "))

if N <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    for fila in range(1, N + 1):
        for columna in range(1, fila + 1):
            print("*", end="")
        print()