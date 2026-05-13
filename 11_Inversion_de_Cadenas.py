palabra = input("Ingresa una palabra: ")

variable_vacia = len(palabra) - 1
palabra_invertida = ""

while variable_vacia >= 0:
    palabra_invertida += palabra[variable_vacia]
    variable_vacia -= 1

print("Palabra invertida:", palabra_invertida)