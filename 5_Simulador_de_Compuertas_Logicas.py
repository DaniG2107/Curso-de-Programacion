def str_to_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"1", "true", "t", "yes", "y"}:
        return True
    if normalized in {"0", "false", "f", "no", "n"}:
        return False
    raise ValueError("Valor booleano inválido")


def nand(a: bool, b: bool) -> bool:
    return not (a and b)


def nor(a: bool, b: bool) -> bool:
    return not (a or b)


def xor(a: bool, b: bool) -> bool:
    return (a or b) and not (a and b)


def xnor(a: bool, b: bool) -> bool:
    return not xor(a, b)


def main() -> None:
    try:
        a = str_to_bool(input("Primer booleano (true/false): "))
        b = str_to_bool(input("Segundo booleano (true/false): "))
        gate = input("Puerta lógica (XOR, NAND, NOR, XNOR): ").strip().upper()
    except ValueError as exc:
        print(f"Entrada inválida: {exc}")
        return

    if gate == "XOR":
        result = xor(a, b)
    elif gate == "NAND":
        result = nand(a, b)
    elif gate == "NOR":
        result = nor(a, b)
    elif gate == "XNOR":
        result = xnor(a, b)
    else:
        print("Puerta lógica inválida. Usa XOR, NAND, NOR o XNOR.")
        return

    print(f"Resultado de {gate}: {result}")


if __name__ == "__main__":
    main()
