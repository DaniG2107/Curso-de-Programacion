numero_secreto = 70

print("¡Bienvenido al juego de adivinar el número!")
print("Intenta adivinar el número secreto.")

while True:
    intento = input("Ingresa tu número: ")

    try:
        intento_numero = int(intento)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    if intento_numero == numero_secreto:
        print("¡Felicidades! Has adivinado el número secreto.")
        break
    elif intento_numero < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    else:
        print("El número secreto es menor. Intenta de nuevo.")