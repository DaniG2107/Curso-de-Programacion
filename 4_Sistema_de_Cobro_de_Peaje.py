print("Esta llegando a un peaje, por favor pagar")

print("seleccione el numero dependediendo de su tipo de vehiculo")

vehiculo = int(input("carro = 1, moto = 2, camion = 3: "))

if vehiculo < 1 or vehiculo >3:
  print("Numero equivocado >:(")

else:
  ("error")


if vehiculo == 1:
   hp = (input("es hora pico? si/no: ").lower())

   if hp == "si":
    print("El costo es de:", 5*1.20,"$")
   
   elif hp == "no":
    print("El costo es de:", 5,"$")

   else:
    print("Error")


if vehiculo == 2:
   hp = (input("es hora pico? si/no: ").lower())

   if hp == "si":
    print("El costo es de:", 2*1.20,"$")
   
   elif hp == "no":
    print("El costo es de:", 2,"$")

   else:
    print("Error")


if vehiculo == 3:
   hp = (input("es hora pico? si/no: ").lower())

   if hp == "si":
    print("El costo es de:", 10*1.20,"$")
   
   elif hp == "no":
    print("El costo es de:", 10,"$")

   else:
    print("Error")