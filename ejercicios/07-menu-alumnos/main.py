"""
Ejercicio 07: Menú de alumnos con listas paralelas.

Crear un programa que permita al usuario elegir entre las siguientes opciones:

1. Agregar un alumno: se solicitan nombre, padrón y nota.
2. Consultar aprobados: mostrar los alumnos con nota mayor o igual a 4.
3. Cantidad de alumnos totales y promedio general.
4. Quitar a un alumno por su padrón.
5. Salir.
"""

OPCIONES: tuple = (
    "Agregar un alumno",
    "Consultar aprobados",
    "Cantidad de alumnos totales y promedio general",
    "Quitar a un alumno",
    "Salir"
)

NOTA_APROBACION: int = 4
OPCION_SALIR: int = 5


def mostrar_menu() -> None:
    for i in range(len(OPCIONES)):
        print(f"{i + 1}) {OPCIONES[i]}")


def agregar_alumnos(nombres: list, padrones: list, notas: list) -> None:
    entrada: str = "S"

    while entrada != "N":
        nombre: str = input("Ingrese el nombre del alumno: ")
        padron: int = int(input(f"Ingrese el padrón del alumno {nombre}: "))
        nota: float = float(input(f"Ingrese la nota del alumno {nombre}: "))

        nombres.append(nombre)
        padrones.append(padron)
        notas.append(nota)

        entrada = input("¿Desea seguir ingresando alumnos S/N?: ").upper()


def mostrar_aprobados(nombres: list, padrones: list, notas: list) -> None:
    print("Alumnos aprobados:")

    for i in range(len(nombres)):
        if notas[i] >= NOTA_APROBACION:
            print(f"- {nombres[i]} (padrón {padrones[i]}): {notas[i]}")


def mostrar_estadisticas(notas: list) -> None:
    if not notas:
        print("No hay alumnos cargados.")
        return

    print(f"Cantidad de alumnos: {len(notas)}")
    print(f"Promedio general: {sum(notas) / len(notas):.2f}")


def quitar_alumno(nombres: list, padrones: list, notas: list) -> None:
    padron: int = int(input("Ingrese el padrón del alumno a eliminar: "))

    if padron in padrones:
        indice: int = padrones.index(padron)
        nombres.pop(indice)
        padrones.pop(indice)
        notas.pop(indice)
        print("Alumno eliminado.")
    else:
        print("No existe un alumno con ese padrón.")


def main() -> None:
    nombres: list = []
    padrones: list = []
    notas: list = []

    mostrar_menu()
    opcion: int = int(input("Ingrese una opción: "))

    while opcion != OPCION_SALIR:
        if opcion == 1:
            agregar_alumnos(nombres, padrones, notas)
        elif opcion == 2:
            mostrar_aprobados(nombres, padrones, notas)
        elif opcion == 3:
            mostrar_estadisticas(notas)
        elif opcion == 4:
            quitar_alumno(nombres, padrones, notas)
        else:
            print("Opción inválida.")

        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))

    print("\nFinalizó el programa")


main()
