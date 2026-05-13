frase = input("Por favor, escribe una frase: ")

vocales = "aeiouAEIOU"

contador = 0

for variable_vacia in frase:
    if variable_vacia in vocales:
        contador += 1

print("La cantidad de vocales en la frase es de: ", contador)