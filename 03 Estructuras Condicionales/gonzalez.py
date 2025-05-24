import random
from statistics import mode, median, mean


def ejercicio_1():
    edad = int(input("Ingrese su edad: "))
    if edad > 18:
        print("Es mayor de edad")

def ejercicio_2():
    nota = float(input("Ingrese su nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

def ejercicio_3():
    numero = int(input("Ingrese un número par: "))
    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

def ejercicio_4():
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("Niño/a")
    elif edad < 18:
        print("Adolescente")
    elif edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

def ejercicio_5():
    contrasenia = input("Ingrese una contraseña: ")
    if 8 <= len(contrasenia) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

def ejercicio_6():
    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)
    if media > mediana > moda:
        print("Sesgo positivo")
    elif media < mediana < moda:
        print("Sesgo negativo")
    elif media == mediana == moda:
        print("Sin sesgo")
    else:
        print("No se puede determinar el sesgo")

def ejercicio_7():
    texto = input("Ingrese una palabra o frase: ")
    if texto[-1].lower() in "aeiou":
        print(texto + "!")
    else:
        print(texto)

def ejercicio_8():
    nombre = input("Ingrese su nombre: ")
    opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para capitalizar: ")
    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.title())
    else:
        print("Opción inválida")

def ejercicio_9():
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    if magnitud < 3:
        print("Muy leve")
    elif magnitud < 4:
        print("Leve")
    elif magnitud < 5:
        print("Moderado")
    elif magnitud < 6:
        print("Fuerte")
    elif magnitud < 7:
        print("Muy Fuerte")
    else:
        print("Extremo")

def ejercicio_10():
    hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
    mes = int(input("Ingrese el número del mes (1-12): "))
    dia = int(input("Ingrese el día del mes: "))
    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    if hemisferio == "N":
        print(estacion_norte)
    elif hemisferio == "S":
        print(estacion_sur)
    else:
        print("Hemisferio inválido")
