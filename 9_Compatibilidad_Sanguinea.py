def normalize_blood_type(group: str, factor: str) -> tuple[str, str]:
    group = group.strip().upper()
    factor = factor.strip().upper()
    if group not in {"A", "B", "AB", "O"}:
        raise ValueError("Grupo sanguíneo inválido")
    if factor not in {"+", "-"}:
        raise ValueError("Factor Rh inválido")
    return group, factor


def is_compatible(donor_group: str, donor_rh: str, receiver_group: str, receiver_rh: str) -> bool:
    if donor_group == "O":
        if donor_rh == "-":
            return True  # O- can donate to anyone
        elif donor_rh == "+":
            if receiver_rh == "+":
                return True  # O+ can donate to + receivers
            else:
                return False
    elif donor_group == "A":
        if donor_rh == "-":
            if receiver_group in {"A", "AB"}:
                return True
            else:
                return False
        elif donor_rh == "+":
            if receiver_group in {"A", "AB"} and receiver_rh == "+":
                return True
            else:
                return False
    elif donor_group == "B":
        if donor_rh == "-":
            if receiver_group in {"B", "AB"}:
                return True
            else:
                return False
        elif donor_rh == "+":
            if receiver_group in {"B", "AB"} and receiver_rh == "+":
                return True
            else:
                return False
    elif donor_group == "AB":
        if donor_rh == "-":
            if receiver_group == "AB" and receiver_rh == "-":
                return True
            else:
                return False
        elif donor_rh == "+":
            if receiver_group == "AB" and receiver_rh == "+":
                return True
            else:
                return False
    return False


def main() -> None:
    try:
        donor_group = input("Grupo sanguíneo del donante (A/B/AB/O): ")
        donor_rh = input("Factor Rh del donante (+/-): ")
        donor_group, donor_rh = normalize_blood_type(donor_group, donor_rh)

        receiver_group = input("Grupo sanguíneo del receptor (A/B/AB/O): ")
        receiver_rh = input("Factor Rh del receptor (+/-): ")
        receiver_group, receiver_rh = normalize_blood_type(receiver_group, receiver_rh)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    if is_compatible(donor_group, donor_rh, receiver_group, receiver_rh):
        print("Transfusión segura.")
    else:
        print("Transfusión no segura.")


if __name__ == "__main__":
    main()