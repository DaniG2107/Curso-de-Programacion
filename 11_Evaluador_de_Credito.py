def evaluate_credit(income: float, debts: float, age: int, delinquency: bool) -> str:
    score = 500  # Base score

    if income > 50000:
        score += 100
    if income > 30000:
        score += 50
    if income < 20000:
        score -= 50

    if debts < 5000:
        score += 50
    if debts < 10000:
        score += 25
    if debts > 20000:
        score -= 100

    if 25 <= age <= 65:
        score += 50
    if age < 18:
        score -= 200
    if age > 70:
        score -= 50

    if delinquency:
        score -= 150

    return "Aprobado" if score >= 600 else "Denegado"


def main() -> None:
    try:
        income = float(input("Ingresos anuales: "))
        debts = float(input("Deudas totales: "))
        age = int(input("Edad: "))
        delinquency = input("¿Tiene morosidad? (sí/no): ").strip().lower() == "sí"
    except ValueError:
        print("Por favor ingresa valores válidos.")
        return

    if income < 0 or debts < 0 or age < 0:
        print("Los valores no pueden ser negativos.")
        return

    result = evaluate_credit(income, debts, age, delinquency)
    print(f"Resultado: {result}")


if __name__ == "__main__":
    main()