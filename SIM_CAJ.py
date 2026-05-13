def main():
    saldo = 1000
    PIN = "1987"
    max_intentos = 3
    intentos = 0
    bloqueado = False

    while intentos < max_intentos:
        ingreso = input("Por favor, ingrese su PIN: ")
        if ingreso == PIN:
            print("PIN correcto. Bienvenido al cajero.")
            break
        else:
            intentos += 1
            print(f"PIN incorrecto. Intento {intentos} de {max_intentos}.")
    else:
        bloqueado = True

    if bloqueado:
        print("El tarjeta ha sido bloqueada por demasiados intentos.")
        return

    while True:
        print("\n--- Menú ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            print(f"Su saldo actual es: ${saldo}")

        elif opcion == "2":
            try:
                monto = float(input("Ingrese el monto a depositar: "))
                if monto <= 0:
                    print("El monto debe ser positivo.")
                else:
                    saldo += monto
                    print(f"Depósito realizado. Nuevo saldo: ${saldo}")
            except ValueError:
                print("Monto inválido. Intente nuevamente.")

        elif opcion == "3":
            try:
                monto = float(input("Ingrese el monto a retirar: "))
                if monto <= 0:
                    print("El monto debe ser positivo.")
                elif monto % 10 != 0:
                    print("El monto debe ser múltiplo de 10.")
                elif monto > saldo:
                    print("Fondos insuficientes.")
                else:
                    cantidad_100 = int(monto // 100)
                    resto = monto % 100

                    cantidad_50 = int(resto // 50)
                    resto = resto % 50

                    cantidad_20 = int(resto // 20)
                    resto = resto % 20

                    cantidad_10 = int(resto // 10)

                    saldo -= monto

                    print(f"Se entregan:")
                    print(f"{cantidad_100} billetes de $100")
                    print(f"{cantidad_50} billetes de $50")
                    print(f"{cantidad_20} billetes de $20")
                    print(f"{cantidad_10} billetes de $10")
                    print(f"Su saldo actual es: ${saldo}")

            except ValueError:
                print("Monto inválido. Intente nuevamente.")

        elif opcion == "4":
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")
            
if __name__ == "__main__":
    main()
