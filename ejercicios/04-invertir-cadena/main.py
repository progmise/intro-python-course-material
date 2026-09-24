"""
Ejercicio 04: Invertir una cadena.

Pedir al usuario que ingrese una cadena de caracteres, invertirla
y mostrarla por consola. Se muestran 3 soluciones posibles.
"""

######### 1° Solución: slicing con paso negativo #########

""" palabra: str = input("Ingrese una palabra: ")

print(f"Palabra original: '{palabra}'")

palabra_invertida: str = palabra[::-1]

print(f"Palabra modificada: '{palabra_invertida}'") """


######### 2° Solución: list() + reverse() + join() #########

""" palabra: str = input("Ingrese una palabra: ")

print(f"Palabra original: '{palabra}'")

letras: list = list(palabra)
letras.reverse()

palabra_invertida: str = "".join(letras)

print(f"Palabra modificada: '{palabra_invertida}'") """


######### 3° Solución: recorrido manual de atrás hacia adelante #########

palabra: str = input("Ingrese una palabra: ")

print(f"Palabra original: '{palabra}'")

palabra_invertida: str = str()

for i in range(len(palabra) - 1, -1, -1):
    print(f"Valor de i: {i}")
    palabra_invertida += palabra[i]

print(f"Palabra modificada: '{palabra_invertida}'")
