"""
Extra 04: List y dict comprehensions.

Ejemplos de creación de listas y diccionarios por comprensión,
comparados con su equivalente escrito manualmente con bucles.
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


######### List comprehension #########

nombres: list = [nota["nombre"] for nota in notas if nota["nota"] > 7]

# Equivalente manual:
# nombres: list = []
# for nota in notas:
#     if nota["nota"] > 7:
#         nombres.append(nota["nombre"])

print(nombres)


######### Dict comprehension #########

lista_de_tuplas: list = [(0, "Rojo"), (1, "Azul"), (2, "Verde"), (3, "Amarillo")]

diccionario: dict = {llave: valor for llave, valor in lista_de_tuplas if llave > 2}

# Equivalente manual:
# diccionario: dict = {}
# for llave, valor in lista_de_tuplas:
#     if llave > 2:
#         diccionario[llave] = valor

print(diccionario)
