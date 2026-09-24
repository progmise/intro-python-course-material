"""
Extra 02: Juego de tablero para dos jugadores.

Juego por turnos sobre un tablero de 4x4: al primer jugador se le
asignan los "unos" y al segundo los "dos". En cada turno se puede
desplazar las piezas propias una celda (a/w/s/d), rotar el tablero
(r) o reflejarlo horizontalmente (t). La partida dura 10 rondas.
"""

import random

tablero: list = [
    ["*", 2, 2, 0],
    [0, 1, 2, 0],
    [0, 1, 2, 0],
    [0, 1, 1, "*"]
]


def mostrar_tablero(tablero: list) -> None:
    for fila in tablero:
        for valor in fila:
            print(" ", valor, end=" ")
        print(" ")


def desplazar_izquierda(numero: int) -> None:
    for fila in tablero:
        for i in range(1, len(fila)):
            if fila[i] == numero and fila[i - 1] == 0:
                fila[i], fila[i - 1] = fila[i - 1], fila[i]
    mostrar_tablero(tablero)


def desplazar_derecha(numero: int) -> None:
    for fila in tablero:
        for i in range(len(fila) - 2, -1, -1):
            if fila[i] == numero and fila[i + 1] == 0:
                fila[i], fila[i + 1] = fila[i + 1], fila[i]
    mostrar_tablero(tablero)


def desplazar_arriba(numero: int) -> None:
    for i in range(1, len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == numero and tablero[i - 1][j] == 0:
                tablero[i][j], tablero[i - 1][j] = tablero[i - 1][j], tablero[i][j]
    mostrar_tablero(tablero)


def desplazar_abajo(numero: int) -> None:
    for i in range(len(tablero) - 2, -1, -1):
        for j in range(len(tablero[i])):
            if tablero[i][j] == numero and tablero[i + 1][j] == 0:
                tablero[i][j], tablero[i + 1][j] = tablero[i + 1][j], tablero[i][j]
    mostrar_tablero(tablero)


def rotar(numero: int) -> None:
    # Rota el tablero completo 90° en sentido horario
    tablero[:] = [list(fila) for fila in zip(*tablero[::-1])]
    mostrar_tablero(tablero)


def invertir(numero: int) -> None:
    # Refleja el tablero completo sobre el eje vertical
    for fila in tablero:
        fila.reverse()
    mostrar_tablero(tablero)


def multiopcion(juego: str, numero: int) -> None:
    if juego == "a":
        desplazar_izquierda(numero)
    elif juego == "s":
        desplazar_abajo(numero)
    elif juego == "w":
        desplazar_arriba(numero)
    elif juego == "d":
        desplazar_derecha(numero)
    elif juego == "r":
        rotar(numero)
    elif juego == "t":
        invertir(numero)


def nombre_jugador(numero: int) -> str:
    return input(f"Ingrese el nombre del jugador {numero}: ")


def sorteo(primer_jugador: str, segundo_jugador: str) -> str:
    if random.randint(1, 2) == 1:
        return primer_jugador
    return segundo_jugador


def main() -> None:
    print("MENU\n[1]Comenzar partida\n[2]Ranking de jugadores\n[3]Terminar juego")
    opcion: int = int(input("Elija una opción: "))

    if opcion == 1:
        primer_jugador: str = nombre_jugador(1)
        segundo_jugador: str = nombre_jugador(2)
        quien_comienza: str = sorteo(primer_jugador, segundo_jugador)

        if quien_comienza == primer_jugador:
            quien_sigue: str = segundo_jugador
        else:
            quien_sigue = primer_jugador

        movimientos: int = 0

        while movimientos != 10:
            print(f"Es el turno de {quien_comienza}, se le asignan los 1(unos)")
            mostrar_tablero(tablero)
            print("[a]Para mover a la izquierda\n[d]Para mover a la derecha\n[w]Para mover hacia arriba\n[s]Para mover hacia abajo\n[r]Para rotar\n[t]Para reflejar al lado contrario")
            juego: str = input("Elija una opción: ")
            multiopcion(juego, 1)

            print(f"Es el turno de {quien_sigue}, se le asignan los 2(dos)")
            mostrar_tablero(tablero)
            print("[a]Para mover a la izquierda\n[d]Para mover a la derecha\n[w]Para mover hacia arriba\n[s]Para mover hacia abajo\n[r]Para rotar\n[t]Para reflejar al lado contrario")
            juego = input("Elija una opción: ")
            multiopcion(juego, 2)

            movimientos += 1


main()
