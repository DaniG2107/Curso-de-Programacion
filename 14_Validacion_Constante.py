numero = float(input("Por favor, ingresa un número positivo: "))

while numero <= 0:
    print("El número debe ser positivo. Inténtalo de nuevo.")
    numero = float(input("Por favor, ingresa un número positivo: "))

print(f"Has ingresado el número positivo: {numero}")