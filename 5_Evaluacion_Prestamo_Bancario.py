print("Bienvenido al BancoChidote.VE ")

edad = int(input("Por favor, indique su edad: "))

if edad > 25:
    ing = int(input("Cuales son sus ingresos?: "))

    if ing > 3000:
     print("Eres apto para el prestamo causa B)")

    elif ing >= 1500 and ing <= 3000:
     print("Aprobado con Aval")

else:
    print("Rechasado ._.")