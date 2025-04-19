def ejercicio_1():
    for i in range(101):
        print(i)

def ejercicio_2():
    numero = input("Ingrese un número entero: ")
    print(len(numero))

def ejercicio_3():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    inicio = min(a, b) + 1
    fin = max(a, b)
    suma = sum(range(inicio, fin))
    print(suma)

def ejercicio_4():
    total = 0
    while True:
        numero = int(input("Ingrese un número (0 para terminar): "))
        if numero == 0:
            break
        total += numero
    print(total)

def ejercicio_5():
    import random
    objetivo = random.randint(0, 9)
    intentos = 0
    while True:
        intento = int(input("Adivine el número (0-9): "))
        intentos += 1
        if intento == objetivo:
            break
    print(intentos)

def ejercicio_6():
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)

def ejercicio_7():
    n = int(input("Ingrese un número entero positivo: "))
    print(sum(range(n + 1)))

def ejercicio_8():
    pares = impares = positivos = negativos = 0
    for _ in range(100):
        n = int(input("Ingrese un número entero: "))
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
    print("Pares:", pares)
    print("Impares:", impares)
    print("Positivos:", positivos)
    print("Negativos:", negativos)

def ejercicio_9():
    total = 0
    for _ in range(100):
        total += int(input("Ingrese un número entero: "))
    print(total / 100)

def ejercicio_10():
    numero = input("Ingrese un número: ")
    print(numero[::-1])