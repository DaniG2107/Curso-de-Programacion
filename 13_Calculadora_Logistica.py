def calculate_logistics_cost(zone: str, weight: float, volume: float, premium: bool) -> float:
    # Paso 1: Costo base por zona
    base_costs = {"A": 100, "B": 150, "C": 200}
    cost = base_costs.get(zone.upper(), 0)
    if cost == 0:
        raise ValueError("Zona inválida")

    # Paso 2: Recargo 50% por peso si > 10 kg
    if weight > 10:
        cost += cost * 0.5

    # Paso 3: Tarifa fija por volumen si > 5 m³
    if volume > 5:
        cost += 50

    # Paso 4: Descuento premium al final (10% si premium)
    if premium:
        cost -= cost * 0.1

    return cost


def main() -> None:
    try:
        zone = input("Zona (A/B/C): ").strip().upper()
        weight = float(input("Peso (kg): "))
        volume = float(input("Volumen (m³): "))
        premium = input("¿Cliente premium? (sí/no): ").strip().lower() == "sí"
    except ValueError:
        print("Por favor ingresa valores válidos.")
        return

    if weight < 0 or volume < 0:
        print("Peso y volumen no pueden ser negativos.")
        return

    try:
        total_cost = calculate_logistics_cost(zone, weight, volume, premium)
        print(f"Costo total: {total_cost:.2f}")
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()