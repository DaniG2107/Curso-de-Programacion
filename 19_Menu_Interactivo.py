def main():
    while True:
        print("\n--- Menú de Operaciones ---")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Multiplicar dos números")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            except ValueError:
                print("Por favor, ingrese números válidos.")
        elif opcion == '2':
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            except ValueError:
                print("Por favor, ingrese números válidos.")
        elif opcion == '3':
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            except ValueError:
                print("Por favor, ingrese números válidos.")
        elif opcion == '4':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()