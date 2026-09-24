"""
Ejercicio 11: Superponer una pieza en un tablero.

Dado un tablero de 4x4 y una "pieza" expresada como lista de
coordenadas (x, y), marcar con 'X' las posiciones ocupadas por
la pieza y mostrar el tablero resultante.
"""


def main() -> None:
    tablero: list = [
        ["*", "*", "*", "*"],
        ["*", "*", "*", "*"],
        ["*", "*", "*", "*"],
        ["*", "*", "*", "*"]
    ]

    pieza: list = [
        [0, 0],
        [0, 1],
        [0, 2]
    ]

    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            for x, y in pieza:
                if x == columna and y == fila:
                    tablero[fila][columna] = "X"

    for fila in tablero:
        print(fila)


main()
