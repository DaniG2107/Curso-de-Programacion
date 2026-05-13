N = int(input("Ingrese el número de términos de Fibonacci a mostrar: "))

a, b = 0, 1

print("Los primeros", N, "términos de Fibonacci son:")

for _ in range(N):
    print(a)
    a, b = b, a + b