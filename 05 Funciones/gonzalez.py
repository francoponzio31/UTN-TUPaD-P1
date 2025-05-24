def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    return 3.14159 * radio * radio

def calcular_perimetro_circulo(radio):
    return 2 * 3.14159 * radio

def segundos_a_horas(segundos):
    return segundos / 3600

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def operaciones_basicas(a, b):
    return a + b, a - b, a * b, a / b

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def calcular_promedio(a, b, c):
    return (a + b + c) / 3
