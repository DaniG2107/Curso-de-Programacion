def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

dia = int(input("¿Qué día es?: "))
mes = int(input("¿Qué mes es?: "))
año = int(input("¿Qué año es?: "))

if mes < 1 or mes > 12:
    print("Mes inválido. Debe estar entre 1 y 12.")
else:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dias = 31
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    else:
        max_dias = 29 if es_bisiesto(año) else 28

    if dia < 1 or dia > max_dias:
        print(f"Día inválido para el mes {mes}. Debe estar entre 1 y {max_dias}.")
    else:
        print(f"Fecha válida: {dia}/{mes}/{año}")
        if mes == 2 and dia == 29:
            print("¡Es un día bisiesto!")