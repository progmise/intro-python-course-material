"""
Ejercicio 10: Conjuntos y generación de informes.

Dada una lista de notas de alumnos (cada registro es un diccionario con
nombre, nota y materia), calcular el promedio de notas por alumno usando
un conjunto para obtener los nombres únicos.
"""

notas: list[dict] = [
    {
        "nombre": "Leonel",
        "nota": 6,
        "materia": "Algoritmos y Programación I"
    },
    {
        "nombre": "Leonel",
        "nota": 4,
        "materia": "Física IA"
    },
    {
        "nombre": "Nicolas",
        "nota": 9,
        "materia": "Algoritmos y Programación I"
    },
    {
        "nombre": "Nicolas",
        "nota": 8,
        "materia": "Algoritmos y Programación I"
    }
]

# Se arma una lista con todos los nombres (con repeticiones)
nombres: list = []

for nota in notas:
    nombres.append(nota["nombre"])

# El conjunto elimina los duplicados
nombres_unicos: set = set(nombres)

informes: list[dict] = []

for nombre in nombres_unicos:
    informe: dict = {
        "nombre": nombre,
        "cantidad_de_notas": 0,
        "acumulador_de_notas": 0.0,
        "promedio": 0.0
    }

    for nota in notas:
        if nota["nombre"] == nombre:
            informe["cantidad_de_notas"] += 1
            informe["acumulador_de_notas"] += nota["nota"]

    informe["promedio"] = informe["acumulador_de_notas"] / informe["cantidad_de_notas"]
    informes.append(informe)

for informe in informes:
    print(f'El alumno {informe["nombre"]} tiene un promedio de {informe["promedio"]:.2f}')
