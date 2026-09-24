"""
Ejercicio 09: Menú de países.

Crear un programa con un menú que permita:

1. Cargar datos de países: nombre, cantidad de registros y dólares invertidos.
2. Mostrar la información de los países con más de 50.000 USD invertidos.
3. Mostrar el índice de USD invertidos totales / registros totales.
4. Salir con '*'.
"""

LIMITE_INVERSION: float = 50000.0
OPCION_SALIR: str = "*"


def hay_pais_duplicado(paises: list, pais_ingresado: str) -> bool:
    """Devuelve True si el país ya figura en la lista cargada."""
    for pais in paises:
        if pais[0] == pais_ingresado:
            return True

    return False


def cargar_datos(paises: list) -> None:
    nombre: str = input("Ingrese el nombre del país (enter para salir): ")

    while nombre:
        if hay_pais_duplicado(paises, nombre):
            print("El país ya fue cargado.")
        else:
            cantidad_de_registros: int = int(input("Ingrese la cantidad de registros: "))
            cantidad_de_dolares: float = float(input("Ingrese la cantidad de dólares invertidos: "))
            paises.append([nombre, cantidad_de_registros, cantidad_de_dolares])

        nombre = input("Ingrese el nombre del país (enter para salir): ")


def mostrar_invertidos(paises: list) -> None:
    print(f"Países con más de {LIMITE_INVERSION:,.0f} USD invertidos:")

    for pais in paises:
        if pais[2] > LIMITE_INVERSION:
            print(f"- {pais[0]}: {pais[1]} registros, {pais[2]:,.2f} USD")


def mostrar_indice(paises: list) -> None:
    registros_totales: int = 0
    dolares_totales: float = 0.0

    for pais in paises:
        registros_totales += pais[1]
        dolares_totales += pais[2]

    if registros_totales == 0:
        print("No hay registros cargados.")
    else:
        print(f"Índice USD invertidos / registros: {dolares_totales / registros_totales:.2f}")


def menu(paises: list) -> None:
    opcion: str = ""

    while opcion != OPCION_SALIR:
        print("1- Cargar datos de países")
        print("2- Mostrar los países con más de 50.000 USD invertidos")
        print("3- Mostrar el índice de USD invertidos totales / registros totales")
        print("*- Salir")
        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            cargar_datos(paises)
        elif opcion == "2":
            mostrar_invertidos(paises)
        elif opcion == "3":
            mostrar_indice(paises)


def main() -> None:
    paises: list = []
    menu(paises)


main()
