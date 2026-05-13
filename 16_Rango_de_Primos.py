N = int(input("Ingresa el valor de N: "))

for num in range(2, N + 1):
    es_primo = True
    
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(num)