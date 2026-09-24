"""
Ejercicio 02: Estructuras de decisión.

Solicitar un número entero e informar si es positivo, negativo o cero.

Se muestran variantes comentadas para comparar `if/else` con `if` consecutivos,
y el efecto de mutar la variable dentro de una rama.
"""

######### 1° Solución: if / else #########

""" numero: int = int(input("Ingrese un valor numérico: "))

if numero > 0:
    print("Número positivo")
else:
    print("Número negativo") """


######### 2° Solución: if consecutivos #########

# Ojo: si dentro del primer `if` se modifica la variable,
# el segundo `if` puede evaluar una condición ya alterada.

""" numero: int = int(input("Ingrese un valor numérico: "))

if numero > 0:
    print("Número positivo")
    numero = -numero

if numero < 0:
    print("Número negativo") """


######### 3° Solución: mutación dentro de la rama #########

# Si numero toma el valor 4, entra al primer `if`, imprime "Número positivo",
# luego numero pasa a valer -4 y se imprime por consola.

""" numero: int = int(input("Ingrese un valor numérico: "))

if numero > 0:
    print("Número positivo")
    numero = -numero
    print(numero)
else:
    print("Número negativo") """


######### 4° Solución: if / elif / else #########

numero: int = int(input("Ingrese un valor numérico: "))

if numero > 0:
    print("Número positivo")
elif numero == 0:
    print("Es igual a 0")
else:
    print("Número negativo")
