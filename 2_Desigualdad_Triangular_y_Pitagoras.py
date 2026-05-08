def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a


def classify_triangle(a: float, b: float, c: float) -> str:
    sides = sorted([a, b, c])
    x, y, z = sides

    if not is_valid_triangle(x, y, z):
        return "No forman un triángulo válido"

    left = x * x + y * y
    right = z * z

    if abs(left - right) < 1e-9:
        return "Triángulo rectángulo"
    elif left > right:
        return "Triángulo agudo"
    else:
        return "Triángulo obtuso"


def main() -> None:
    try:
        a = float(input("Lado 1: "))
        b = float(input("Lado 2: "))
        c = float(input("Lado 3: "))
    except ValueError:
        print("Por favor ingresa números válidos.")
        return

    if not is_valid_triangle(a, b, c):
        print("Las longitudes no forman un triángulo válido.")
        return

    print(classify_triangle(a, b, c))


if __name__ == "__main__":
    main()
