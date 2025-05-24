def ejercicio_1():
    return list(range(4, 101, 4))

def ejercicio_2():
    lista = ["libro", "café", "música", "película", "chocolate"]
    return lista[-2]

def ejercicio_3():
    lista_vacia = []
    lista_vacia.append("sol")
    lista_vacia.append("luna")
    lista_vacia.append("estrella")
    return lista_vacia

def ejercicio_4():
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"
    animales[-1] = "oso"
    return animales

def ejercicio_5():
    # numeros = [8, 15, 3, 22, 7]
    # numeros.remove(max(numeros))
    # print(numeros)
    "El programa elimina el número mayor de la lista, e imprime la lista resultante."

def ejercicio_6():
    lista = list(range(10, 31, 5))
    return lista[:2]

def ejercicio_7():
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1:3] = ["camioneta", "coupe"]
    return autos

def ejercicio_8():
    dobles = []
    dobles.append(5 * 2)
    dobles.append(10 * 2)
    dobles.append(15 * 2)
    return dobles

def ejercicio_9():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras[0].remove("pan")
    return compras

def ejercicio_10():
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    return lista_anidada
