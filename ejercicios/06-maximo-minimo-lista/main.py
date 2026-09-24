"""
Ejercicio 06: Máximo y mínimo de una lista.

Dada una lista de números enteros, encontrar el máximo y el mínimo
y mostrarlos por consola. Se muestran varias soluciones posibles.
"""

numeros: list = [1, 4, 2, 3, 99, 100]


######### 1° Solución: funciones built-in max() y min() #########

""" numero_maximo: int = max(numeros)
numero_minimo: int = min(numeros)

print(f"El número máximo de la lista de números es: {numero_maximo}")
print(f"El número mínimo de la lista de números es: {numero_minimo}") """


######### 2° Solución: recorrido manual en un solo bucle #########

""" numero_maximo: int = numeros[0]
numero_minimo: int = numeros[0]

for numero in numeros:
    if numero > numero_maximo:
        numero_maximo = numero

    if numero < numero_minimo:
        numero_minimo = numero

print(f"El número máximo de la lista de números es: {numero_maximo}")
print(f"El número mínimo de la lista de números es: {numero_minimo}") """


######### 3° Solución: con funciones #########

def calcular_maximo(lista_de_numeros: list) -> int:
    numero_maximo: int = lista_de_numeros[0]

    for numero in lista_de_numeros:
        if numero > numero_maximo:
            numero_maximo = numero

    return numero_maximo


def calcular_minimo(lista_de_numeros: list) -> int:
    numero_minimo: int = lista_de_numeros[0]

    for numero in lista_de_numeros:
        if numero < numero_minimo:
            numero_minimo = numero

    return numero_minimo


numero_maximo: int = calcular_maximo(numeros)
numero_minimo: int = calcular_minimo(numeros)

print(f"El número máximo de la lista de números es: {numero_maximo}")
print(f"El número mínimo de la lista de números es: {numero_minimo}")
