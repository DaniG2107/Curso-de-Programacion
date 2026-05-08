print("ES HORA DE-DE-DEL DUELO")

jugada1 = input("Jugador 1, piedra, papel o tijeras: ").lower()
jugada2 = input("Jugador 2, piedra, papel o tijeras: ").lower()

if jugada1 == "piedra" and jugada2 == "piedra":
    print("EMPATE")

elif jugada1 == "piedra" and jugada2 == "tijeras":
    print("JUGADOR 1 WIN's")

elif jugada1 == "piedra" and jugada2 == "papel":
    print("JUGADOR 2 WIN's")

elif jugada1 == "papel" and jugada2 == "piedra":
    print("JUGADOR 1 WIN's")

elif jugada1 == "papel" and jugada2 == "papel":
    print("EMPATE")

elif jugada1 == "papel" and jugada2 == "tijeras":
    print("JUGADOR 2 WIN's")

elif jugada1 == "tijeras" and jugada2 == "piedra":
    print("JUGADOR 2 WIN's")

elif jugada1 == "tijeras" and jugada2 == "papel":
    print("JUGADOR 1 WIN's")

elif jugada1 == "tijeras" and jugada2 == "tijeras":
    print("EMPATE")

else:
    print("ERROR")