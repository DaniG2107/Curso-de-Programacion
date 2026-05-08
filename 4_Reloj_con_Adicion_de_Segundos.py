def add_seconds_to_time(hour: int, minute: int, second: int, add_seconds: int) -> tuple[int, int, int]:
    total_seconds = hour * 3600 + minute * 60 + second + add_seconds
    total_seconds %= 24 * 3600

    new_hour = total_seconds // 3600
    new_minute = (total_seconds % 3600) // 60
    new_second = total_seconds % 60

    return new_hour, new_minute, new_second


def main() -> None:
    try:
        hour = int(input("Hora (0-23): "))
        minute = int(input("Minuto (0-59): "))
        second = int(input("Segundo (0-59): "))
        add_seconds = int(input("Segundos a adicionar: "))
    except ValueError:
        print("Por favor ingresa valores enteros válidos.")
        return

    if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
        print("La hora debe estar en formato 24 horas: 0-23, 0-59, 0-59.")
        return

    new_hour, new_minute, new_second = add_seconds_to_time(hour, minute, second, add_seconds)
    print(f"Hora resultante: {new_hour:02d}:{new_minute:02d}:{new_second:02d}")


if __name__ == "__main__":
    main()
