"""
Extra 05: Lambdas, ordenamiento y filtrado.

Ejemplos de uso de funciones lambda como criterio de ordenamiento
(.sort() / sorted()) y de filtrado (filter()), sobre estructuras
simples (listas de valores) y complejas (listas de diccionarios
y listas de listas).

La mayoría de los ejemplos están comentados: descomentar de a uno
para probarlos y observar las diferencias.
"""


############## LAMBDAS ##############

# Una lambda es una función anónima de una sola expresión.
# Estas definiciones son equivalentes:

# def es_mayor_a_50(numero: int) -> bool:
#     return numero > 50

es_mayor_a_50 = lambda numero: numero > 50

print(es_mayor_a_50(100))
print(es_mayor_a_50(-1))

# Funciones "normales" que también sirven como criterio:
# def obtener_valor_a_comparar_en_diccionario(diccionario: dict) -> int:
#     return diccionario['cantidad_de_contenedores']

# def obtener_valor_a_comparar_en_lista(lista: list) -> float:
#     return lista[3]


############## ORDENAMIENTO ##############

#################################
###### ESTRUCTURAS SIMPLES ######
#################################

cadenas: list[str] = [
    "Hola", "Mundo", "Hello", "World",
    "Bye", "Adios", "hola", "mundo",
    "perro", "gato", "1995", "2022"
]

numeros: list[int] = [
    50, 11, 56, 3, 9,
    74, 88, 24, 30, 99,
    1, 67, 5, 33, 71
]


###### Método .sort() ######

# Ordena la lista in-place (modifica la original).

# Ordeno ascendentemente
# cadenas.sort()
# numeros.sort()

# print(cadenas)
# print(numeros)

# Ordeno descendentemente
# cadenas.sort(reverse=True)
# numeros.sort(reverse=True)

# print(cadenas)
# print(numeros)


###### Función sorted() ######

# Devuelve una NUEVA lista ordenada (la original queda intacta).

# Ordeno ascendentemente
# cadenas_ordenadas: list[str] = sorted(cadenas)
# numeros_ordenados: list[int] = sorted(numeros)

# print(cadenas_ordenadas)
# print(numeros_ordenados)

# Ordeno descendentemente
# cadenas_ordenadas: list[str] = sorted(cadenas, reverse=True)
# numeros_ordenados: list[int] = sorted(numeros, reverse=True)

# print(cadenas_ordenadas)
# print(numeros_ordenados)


#################################
##### ESTRUCTURAS COMPLEJAS #####
#################################

barcos: list[dict] = [
    {
        'nombre_del_barco': "Costa S.A.",
        'cantidad_de_contenedores': 30,
        'peso_de_cada_contenedor': 4000.0,
        'valor_de_mercaderia_de_cada_contenedor': 90000.0,
        'origen_de_contenedores': "España"
    },
    {
        'nombre_del_barco': "Guido S.A.",
        'cantidad_de_contenedores': 40,
        'peso_de_cada_contenedor': 3000.0,
        'valor_de_mercaderia_de_cada_contenedor': 70000.0,
        'origen_de_contenedores': "Argentina"
    },
    {
        'nombre_del_barco': "Bruno S.A.",
        'cantidad_de_contenedores': 100,
        'peso_de_cada_contenedor': 1000.0,
        'valor_de_mercaderia_de_cada_contenedor': 30000.0,
        'origen_de_contenedores': "Brasil"
    },
    {
        'nombre_del_barco': "Lanzillota S.A.",
        'cantidad_de_contenedores': 10,
        'peso_de_cada_contenedor': 7000.0,
        'valor_de_mercaderia_de_cada_contenedor': 130000.0,
        'origen_de_contenedores': "España"
    },
    {
        'nombre_del_barco': "Esperon S.A.",
        'cantidad_de_contenedores': 150,
        'peso_de_cada_contenedor': 500.0,
        'valor_de_mercaderia_de_cada_contenedor': 15000.0,
        'origen_de_contenedores': "Alemania"
    }
]

notas: list[list] = [
    [105183, 'Leonel', 'Algoritmos y Programación I', 7.0, True],
    [106718, 'Lautaro', 'Algoritmos y Programación II', 5.5, True],
    [103001, 'Ezequiel', 'Análisis Matemático', 3, False],
    [107863, 'Gisela', 'Física IA', 9, True],
    [99453, 'Federico', 'Algebra II', 2, False]
]


###### Método .sort() con criterio (key) ######

# ¿Bajo qué criterio ordena, si ya no son datos simples?
# Se lo indicamos con el parámetro key, que recibe una función.

# Ordeno ascendentemente
# barcos.sort(key=lambda barco: barco['cantidad_de_contenedores'])
# notas.sort(key=lambda nota: nota[3])

# for barco in barcos:
#     print(barco)

# print()

# for nota in notas:
#     print(nota)

# Ordeno descendentemente
# barcos.sort(key=lambda barco: barco['cantidad_de_contenedores'], reverse=True)
# notas.sort(key=lambda nota: nota[3], reverse=True)


###### Función sorted() con criterio (key) ######

# Ordeno ascendentemente
# barcos_ordenados: list = sorted(barcos, key=lambda barco: barco['nombre_del_barco'])
# notas_ordenadas: list = sorted(notas, key=lambda nota: nota[1])

# for barco in barcos_ordenados:
#     print(barco)

# print()

# for nota in notas_ordenadas:
#     print(nota)


############## FILTRADO ##############

# filter(criterio, iterable) devuelve un iterador con los elementos
# que cumplen la condición; se materializa con list().

#################################
###### ESTRUCTURAS SIMPLES ######
#################################

# numeros_mayores_a_50: list[int] = list(filter(lambda numero: numero > 50, numeros))

# for numero in numeros_mayores_a_50:
#     print(numero)


#################################
##### ESTRUCTURAS COMPLEJAS #####
#################################

# notas_aprobadas: list[list] = list(filter(lambda nota: nota[4], notas))

# for nota in notas_aprobadas:
#     print(nota)
