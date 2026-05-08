def has_x_won(a1: str, a2: str, a3: str, b1: str, b2: str, b3: str, c1: str, c2: str, c3: str) -> bool:
    return (
        (a1 == 'X' and a2 == 'X' and a3 == 'X') or  # Fila 1
        (b1 == 'X' and b2 == 'X' and b3 == 'X') or  # Fila 2
        (c1 == 'X' and c2 == 'X' and c3 == 'X') or  # Fila 3
        (a1 == 'X' and b1 == 'X' and c1 == 'X') or  # Columna 1
        (a2 == 'X' and b2 == 'X' and c2 == 'X') or  # Columna 2
        (a3 == 'X' and b3 == 'X' and c3 == 'X') or  # Columna 3
        (a1 == 'X' and b2 == 'X' and c3 == 'X') or  # Diagonal 1
        (a3 == 'X' and b2 == 'X' and c1 == 'X')     # Diagonal 2
    )


def main() -> None:
    print("Ingresa el tablero (X, O, o vacío):")
    a1 = input("a1: ").strip().upper()
    a2 = input("a2: ").strip().upper()
    a3 = input("a3: ").strip().upper()
    b1 = input("b1: ").strip().upper()
    b2 = input("b2: ").strip().upper()
    b3 = input("b3: ").strip().upper()
    c1 = input("c1: ").strip().upper()
    c2 = input("c2: ").strip().upper()
    c3 = input("c3: ").strip().upper()

    if has_x_won(a1, a2, a3, b1, b2, b3, c1, c2, c3):
        print("X ganó.")
    else:
        print("X no ganó.")


if __name__ == "__main__":
    main()