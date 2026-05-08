print("Luego de diversas cosas (pereza literaria) has conseguido un trabajo de medio tiempo en un McDonald’s para poder pagarte al fin una PC en condiciones, para la salida del GTA VI. podras sobrevivir tu jornada de 6 horas y conseguir tu pago?")

print("Al llegar, tu jefe te recibe con instrucciones y te indica qué tareas puedes realizar.")

print("Que decides hacer este dia?")

op1 = input("hasar en la parrila la CARNE, buscar suministros en el CONGELADOR o LIMPIAR el local: ").lower()



if op1 == "carne":
    op2 = input("usar parrilla ELECTRICA, usar parrilla a CARBON o usar un LANZALLAMAS: ").lower()
    
    if op2 == "carbon":
        op3 = input("usar carne NORMAL, usar carne VEGANA o usar un DEDO de Sukuna: ").lower()

        if op3 == "normal":
            op4 = input("poner la carne en pan de HAMBURGUESA, un pan FRANCES o un OVNI: ").lower()

            if op4 == "hamburguesa":
                op5 = input("HACER las papas fritas, usar papas PREHECHAS o usar YUCA: ").lower()

                if op5 == "prehechas":
                    op6 = input("hecharle SAL, hecharle PIMIENTA o hecharle COBALTO40: ").lower()

                    if op6 == "pimienta":
                        print("Sales exitoso de tu trabajo siendo un campeon, llendo ya mismo a buscar la pc cuando... un carro te atropella y mueres antes de conseguir tu querido GTA IV, FIN (semi-canon).")

                    elif op6 == "cobalto40":
                        print("NO MAMES ES COBALTO40, QUE PEDO CONTIGO?, GAME OVER.")
    
                    elif op6 == "sal":
                        print("al final no era sal, mas bien veneno para ratas,fuiste demandado y encarcelado por matar a tu clientela, GAME OVER.")

                elif op5 == "yuca":
                    print("la yuca que agarraste estaba contaminada por sida, lamentablemente ya no hay salvacion para ti, GAME OVER.")
    
                elif op5 == "hacer":
                    print("pones las papas en la freidora, pero no te das cuenta de que la temperatura estaba por encima de los niveles aceptables y eres totalmentecubierto por aceite hirviendo muriendo en gran agonia, GAME OVER.")

            elif op4 == "ovni":
                print("los aliens se llevan tus hamburguesas, al no tener mas hamburguesas eres despedido por ser pendejo, GAME OVER.")
    
            elif op4 == "frances":
                print("intentas meter la hamburguesa en un pan frances y eres inmediatamente deportado fuera del pais por un acto terrorista tan terrible, GAME OVER.")

        elif op3 == "dedo":
            print("cuando intentas tocar el dedo y eres transportado a una expansion de dominio donde eres picado en miles de pedazos instantaneamente, GAME OVER.")
    
        elif op3 == "vegana":
            print("cuando la calientas esta masa amorfa de la naturaleza salta en ti acabando contigo de manera espantoza (te comio a ti we), GAME OVER.")

    elif op2 == "lanzallamas":
        print("cocinas la hamburguesa con el lanzallamas, se pasa de coccion (para nada obvio...) y el que limpia te mete un escopetazo por darle mas trabajo del que le pagan, GAME OVER.")
    
    elif op2 == "electrica":
        print("intentas usar la parrila cuando te das cuenta de que el suelo estaba mojado y al hacer corto circuito quemas el edificio (como que ya no hay chamba), GAME OVER.")



if op1 == "congelador":
    op2 = input("buscar NUGGETS, PAPAS o HELADO: ").lower()
    
    if op2 == "helado":
        op3 = input("buscas la zona en la que se guardan los postres frios decides tomar helado de CHOCOLATE, FRESA o MANTECADO: ").lower()

        if op3 == "chocolate":
            op4 = input("aprovechas para buscar algun toping para los mismos eliges GALLETAS, CHISPAS de colores o MALVADISCOS: ").lower()

            if op4 == "malvadiscos":
                op5 = input("vas a servir los helados cuando te topas con un compañero enojado prefieres HABLARLE, pasar de LARGO o PATEARLO").lower()

                if op5 == "largo":
                    op6 = input("estas a punto de salir de tu turno y te consigues dinero tirado en el suelo que haaces AGARRARLO, IGNORARLO o prenderle FUEGO").lower()

                    if op6 == "agarrarlo":
                        print("Luego de tantas cosas ales exitoso de tu trabajo (con un poco mas de dinero) y siendo un campeon, llendo ya mismo a buscar la pc cuando... un carro te atropella y eres llevado al hospital antes de conseguir tu querido GTA IV. Parece que alguien tendra que esperar mas tiempo, FIN (canon).")

                    elif op6 == "quemarlo":
                        print("eres malvado y quemas el dinero, dudo mucho de tus facultades mentales y te obligo a reiniciar, GAME OVER.")
    
                    elif op6 == "ignorarlo":
                        print("ignoras el dinero y al irte eres atracado por dos pandilleros robandote todo, parace que tendras que trabajar mas... GAME OVER.")

                elif op5 == "patearlo":
                    print("luego de hacer esa babosada eres baleado por tu compañero que se habia traido un AK-47 a la chamba, es una pena terrible...GAME OVER.")
    
                elif op5 == "hablarle":
                    print("intentas hablarle a tu compañero cuando eres golpeado por el recuerdo de que no sabes entrablar conversacion con otras personas y mueres de depresion, GAME OVER.")

            elif op4 == "chispas":
                print("intentas alcanzar las chispas hasta que por un mal movimiento una caja pesado cae sobre ti aplastandote, GAME OVER.")
    
            elif op4 == "galletas":
                print("tomas las galletas cuando te das cuenta que una colmena de hormigas anidaba ahi, eres picado hasta la muerte, GAME OVER.")

        elif op3 == "mantecado":
            print("eso es demasiado basico, no mereces avanzar mas... GAME OVER.")
    
        elif op3 == "fresa":
            print("eres bulleado por todos al saber de tus gustos curiosos y decides abandonar el trabajo, GAME OVER.")

    elif op2 == "papas":
        print("ver las papas te llena de recuerdos de como tu padre te abandono y decides retirarte hasta proximo aviso, GAME OVER.")
    
    elif op2 == "nuggets":
        print("intentas tomar los nuggets cuando sale un horda de pollos enojado yu eres pisoteado hasta la muerte, GAME OVER.")



if op1 == "limpiar":
    op2 = print("NAH, te da pereza y abandonas tus sueños y esperanzas, FIN (no-canon).")