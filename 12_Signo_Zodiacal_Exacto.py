def is_valid_date(day: int, month: int) -> bool:
    if month < 1 or month > 12:
        return False
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 1 <= day <= days_in_month[month - 1]


def get_zodiac_sign(day: int, month: int) -> str:
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Tauro"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Géminis"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cáncer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Escorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagitario"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricornio"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Acuario"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Piscis"
    else:
        return "Fecha inválida"


def main() -> None:
    try:
        day = int(input("Día: "))
        month = int(input("Mes (1-12): "))
    except ValueError:
        print("Por favor ingresa números enteros.")
        return

    if not is_valid_date(day, month):
        print("Fecha inválida.")
        return

    sign = get_zodiac_sign(day, month)
    print(f"Signo zodiacal: {sign}")


if __name__ == "__main__":
    main()