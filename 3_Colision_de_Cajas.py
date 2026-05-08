def rectangles_overlap(rect1: tuple[float, float, float, float], rect2: tuple[float, float, float, float]) -> bool:
    x1_min, y1_min, x1_max, y1_max = rect1
    x2_min, y2_min, x2_max, y2_max = rect2

    return not (
        x1_max < x2_min or
        x2_max < x1_min or
        y1_max < y2_min or
        y2_max < y1_min
    )


def read_rectangle(rect_number: int) -> tuple[float, float, float, float]:
    print(f"Rectángulo {rect_number}")
    x_min = float(input("  Coordenada x inferior: "))
    y_min = float(input("  Coordenada y inferior: "))
    x_max = float(input("  Coordenada x superior: "))
    y_max = float(input("  Coordenada y superior: "))

    if x_min > x_max or y_min > y_max:
        raise ValueError("Las coordenadas inferiores deben ser menores o iguales a las superiores.")

    return x_min, y_min, x_max, y_max


def main() -> None:
    try:
        rect1 = read_rectangle(1)
        rect2 = read_rectangle(2)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    if rectangles_overlap(rect1, rect2):
        print("Los rectángulos colisionan (se superponen).")
    else:
        print("Los rectángulos no colisionan.")


if __name__ == "__main__":
    main()
