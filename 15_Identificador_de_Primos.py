numero = int(input("Ingresa un número: "))

if numero < 2:
    print(f"{numero} no es un número primo.")
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"{numero} no es un número primo, ya que es divisible por {i}.")
            break
    else:
        print(f"{numero} es un número primo.")