print("Bienvenido a nuestra tienda")

compu = 100
vestir = 15

categoria = input("De que categoria desea comprar?: ").lower()


if categoria == "electronica":
    cantidad = int(input("Cuantos productos llevara?: "))

    if cantidad < 3:
        print("Serian", cantidad * compu)

    elif cantidad >= 3:
        print("Serian", cantidad * compu * 0.85)

    else:
        print("Error")


if categoria == "ropa":
    cantidad = int(input("Cuantos productos llevara?: "))

    if cantidad < 5:
        print("Serian", cantidad * vestir)

    elif cantidad >= 5:
        print("Serian", cantidad * vestir * 0.90)

    else:
        print("Error")