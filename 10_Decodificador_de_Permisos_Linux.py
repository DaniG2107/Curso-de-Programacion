def decode_permissions(perm: int) -> str:
    permissions = []
    if perm & 4:  # Lectura
        permissions.append("Lectura")
    if perm & 2:  # Escritura
        permissions.append("Escritura")
    if perm & 1:  # Ejecución
        permissions.append("Ejecución")
    return ", ".join(permissions) if permissions else "Ninguno"


def main() -> None:
    try:
        perm = int(input("Ingresa un número del 0 al 7: "))
    except ValueError:
        print("Por favor ingresa un número entero.")
        return

    if not (0 <= perm <= 7):
        print("El número debe estar entre 0 y 7.")
        return

    result = decode_permissions(perm)
    print(f"Permisos: {result}")


if __name__ == "__main__":
    main()