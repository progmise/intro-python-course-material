"""
Código repetido 02: Fragmento con código duplicado (ANTES de refactorizar).

Fragmento extraído del juego de crucigrama (ver ../03-crucigrama/) usado
en clase para aplicar el "Algoritmo para quitar código repetido"
(ver ../01-algoritmo-para-quitar-codigo-repetido/).

⚠️ Este archivo NO es ejecutable: es un fragmento con dependencias
externas, conservado a propósito para su análisis.
"""


def cargar_palabras(indice_inicial_de_palabras: int, indice_final_de_palabras: int, indice_vertical_inicial: int, indice_vertical_final: int, indice_horizontal_inicial: int, indice_horizontal_final: int, indice_auxiliar_inicial: int, indice_auxiliar_final: int):

    for j in range(indice_auxiliar_inicial,inicial_de_palabras, indice_final_de_palabras):
        coordenadas_de_horizontales = []
        fila_horizontal_random = randint(indice_vertical_inicial, indice_vertical_final)
        columna_horizontal_random = randint(indice_horizontal_inicial, indice_horizontal_final)

        while(fila_horizontal_random in lista_de_filas):
            fila_horizontal_random = randint(indice_, indice_auxiliar_final)

        lista_de_filas.append(fila_horizontal_random)
        coordenadas_de_horizontales.append(fila_horizontal_random)
        coordenadas_de_horizontales.append(columna_horizontal_random)
        lista_de_coordenadas.append(coordenadas_de_horizontales)
        tablero[fila_horizontal_random][columna_horizontal_random] = diccionario_hasta_l[j]
        columna_horizontal_random += 1
        for y in range(1, len(palabras_elegidas[j][0])):
            tablero[fila_horizontal_random][columna_horizontal_random] = " "
            columna_horizontal_random += 1
