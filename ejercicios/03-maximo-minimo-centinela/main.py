"""
Ejercicio 03: Máximo y mínimo con centinela.

Solicitar el ingreso de números hasta que el usuario ingrese '*'
y luego mostrar el máximo y el mínimo de los valores cargados.
"""

entrada: str = input("Ingrese un número o '*' para finalizar: ")

maximo: int = 0
minimo: int = 0
hubo_ingresos: bool = False

while entrada != "*":
    numero: int = int(entrada)

    if not hubo_ingresos:
        maximo = numero
        minimo = numero
        hubo_ingresos = True

    if numero > maximo:
        maximo = numero

    if numero < minimo:
        minimo = numero

    entrada = input("Ingrese un número o '*' para finalizar: ")

if hubo_ingresos:
    print(f"El número máximo es: {maximo}")
    print(f"El número mínimo es: {minimo}")
else:
    print("No se ingresaron números.")
