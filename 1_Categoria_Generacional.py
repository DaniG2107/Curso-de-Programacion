año = int(input("Ingrese su año de nacimiento: "))
edad = 2023 - año

if edad >= 1946 and edad <= 1964:
    print("Usted es Baby Boomer")
    
elif edad >= 1965 and edad <= 1980:
    print("Usted es Gen X")

elif edad >= 1981 and edad <= 1996:
    print("Usted es Millennial")

elif edad >= 1997 and edad <= 2012:
    print("Usted es Gen Z")

else:
    print("Usted es Gen Alpha auuuh XD")