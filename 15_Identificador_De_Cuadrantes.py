def identify_quadrant(x: float, y: float) -> str:
    if x == 0.0 and y == 0.0:
        return "Origen"
    elif x == 0.0:
        return "Eje Y"
    elif y == 0.0:
        return "Eje X"
    elif x > 0.0 and y > 0.0:
        return "Cuadrante I"
    elif x < 0.0 and y > 0.0:
        return "Cuadrante II"
    elif x < 0.0 and y < 0.0:
        return "Cuadrante III"
    elif x > 0.0 and y < 0.0:
        return "Cuadrante IV"
    else:
        return "Indeterminado"


def main() -> None:
    try:
        x = float(input("Coordenada x: "))
        y = float(input("Coordenada y: "))
    except ValueError:
        print("Por favor ingresa números válidos.")
        return

    result = identify_quadrant(x, y)
    print(f"Posición: {result}")


if __name__ == "__main__":
    main()