def calculate_tax(income: float) -> float:
    tax = 0.0

    if income > 10000:
        taxable = min(income, 30000) - 10000
        tax += taxable * 0.15

    if income > 30000:
        taxable = min(income, 60000) - 30000
        tax += taxable * 0.25

    if income > 60000:
        taxable = income - 60000
        tax += taxable * 0.35

    return tax


def main() -> None:
    try:
        income = float(input("Ingresa el ingreso anual: "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        return

    if income < 0:
        print("El ingreso no puede ser negativo.")
        return

    tax = calculate_tax(income)
    print(f"Impuesto total: {tax:.2f}")


if __name__ == "__main__":
    main()
