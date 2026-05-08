def normalize_choice(choice: str) -> str:
    normalized = choice.strip().lower()
    if normalized in {"piedra", "papel", "tijera", "lagarto", "spock"}:
        return normalized
    raise ValueError("Elección inválida")


def determine_winner(choice1: str, choice2: str) -> str:
    if choice1 == choice2:
        return "Empate"

    win_conditions = (
        (choice1 == "tijera" and choice2 in {"papel", "lagarto"}) or
        (choice1 == "papel" and choice2 in {"piedra", "spock"}) or
        (choice1 == "piedra" and choice2 in {"lagarto", "tijera"}) or
        (choice1 == "lagarto" and choice2 in {"spock", "papel"}) or
        (choice1 == "spock" and choice2 in {"tijera", "piedra"})
    )

    return "Jugador 1 gana" if win_conditions else "Jugador 2 gana"


def main() -> None:
    try:
        player1 = normalize_choice(input("Jugador 1 (piedra/papel/tijera/lagarto/spock): "))
        player2 = normalize_choice(input("Jugador 2 (piedra/papel/tijera/lagarto/spock): "))
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    resultado = determine_winner(player1, player2)
    print(resultado)


if __name__ == "__main__":
    main()
