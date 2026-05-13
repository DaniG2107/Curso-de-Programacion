def calcular_mcd(a, b):
    while b != 0:
        residuo = a % b
        a = b
        b = residuo
    return a

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = calcular_mcd(num1, num2)

print(f"El MCD de {num1} y {num2} es: {resultado}")