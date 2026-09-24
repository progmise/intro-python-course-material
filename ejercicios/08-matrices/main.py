"""
Ejercicio 08: Matrices (listas de listas).

1) Recorrido de una matriz por índices y por elementos.
2) El error clásico de crear una matriz con multiplicación de listas.
3) Creación correcta de una matriz con bucles anidados.
"""

CANTIDAD_DE_FILAS: int = 4
CANTIDAD_DE_COLUMNAS: int = 4


######### 1) Recorrido de una matriz #########

lista_de_numeros: list = [
    ["01", "02", "03", "04"],
    ["05", "06", "07", "08"],
    ["09", "10", "11", "12"],
    ["13", "14", "15", "16"]
]

# Por índices
for i in range(len(lista_de_numeros)):
    for j in range(len(lista_de_numeros[i])):
        print(lista_de_numeros[i][j])

# Por elementos
for fila in lista_de_numeros:
    for numero in fila:
        print(numero)


######### 2) Forma INCORRECTA de crear una matriz #########

# Al multiplicar la lista externa, todas las "filas" son la MISMA lista:
# modificar una celda modifica esa posición en todas las filas.

matriz_incorrecta: list = [[0] * CANTIDAD_DE_COLUMNAS] * CANTIDAD_DE_FILAS

print("\nAntes de la modificación\n")

for fila in matriz_incorrecta:
    print(fila)

matriz_incorrecta[0][0] = 3

print("\nDespués de la modificación (el 3 aparece en TODAS las filas)\n")

for fila in matriz_incorrecta:
    print(fila)


######### 3) Forma correcta de crear una matriz #########

matriz: list = []

for x in range(CANTIDAD_DE_FILAS):
    fila: list = []

    for y in range(CANTIDAD_DE_COLUMNAS):
        fila.append(0)

    matriz.append(fila)

# Equivalente con list comprehension:
# matriz = [[0] * CANTIDAD_DE_COLUMNAS for _ in range(CANTIDAD_DE_FILAS)]

print("\nAntes de la modificación\n")

for fila in matriz:
    print(fila)

matriz[0][0] = 3

print("\nDespués de la modificación (solo cambia la fila 0)\n")

for fila in matriz:
    print(fila)
