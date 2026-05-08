def validate_octet(value: str) -> int:
    octet = int(value)
    if 0 <= octet <= 255:
        return octet
    raise ValueError("Octeto fuera de rango")


def classify_ip(o1: int, o2: int, o3: int, o4: int) -> str:
    if 0 <= o1 <= 255 and 0 <= o2 <= 255 and 0 <= o3 <= 255 and 0 <= o4 <= 255:
        if 0 <= o1 <= 127:
            return "Clase A"
        elif 128 <= o1 <= 191:
            return "Clase B"
        elif 192 <= o1 <= 223:
            return "Clase C"
        elif 224 <= o1 <= 239:
            return "Clase D"
        elif 240 <= o1 <= 255:
            return "Clase E"
        else:
            return "Clase desconocida"
    else:
        return "Octeto inválido"


def main() -> None:
    try:
        o1 = validate_octet(input("Octeto 1: "))
        o2 = validate_octet(input("Octeto 2: "))
        o3 = validate_octet(input("Octeto 3: "))
        o4 = validate_octet(input("Octeto 4: "))
    except ValueError:
        print("Error: cada octeto debe ser un número entero entre 0 y 255.")
        return

    resultado = classify_ip(o1, o2, o3, o4)
    print(f"Clase IP: {resultado}")


if __name__ == "__main__":
    main()
