celsius = int(input("coloque la temperatura del agua: "))

if celsius < 0:
    print("es un hielo mi pana")
elif celsius == 0:
    print("ta tibia")
elif celsius > 0:
    print("ta que arde")
else:
    print("eso ni agua es")