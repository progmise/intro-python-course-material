"""
Ejercicio 05: Palabras intercaladas.

El usuario ingresa una cadena de caracteres con dos palabras intercaladas:
los caracteres en posiciones pares forman la primera palabra y los de
posiciones impares, la segunda. Se pide separarlas y mostrarlas.

Ejemplo: "hcohlaau" -> "hola" + "chau"
"""

######### 1° Solución: slicing con paso #########

""" palabra_intercalada: str = "hcohlaau"

primer_palabra: str = palabra_intercalada[0::2]
segunda_palabra: str = palabra_intercalada[1::2]

print(f"Primer palabra: {primer_palabra}")
print(f"Segunda palabra: {segunda_palabra}") """


######### 2° Solución: dos bucles con range() y paso 2 #########

""" palabra_intercalada: str = "hcohlaau"

primer_palabra: str = str()
segunda_palabra: str = str()

for i in range(0, len(palabra_intercalada), 2):
    primer_palabra += palabra_intercalada[i]

for i in range(1, len(palabra_intercalada), 2):
    segunda_palabra += palabra_intercalada[i]

print(f"Primer palabra: {primer_palabra}")
print(f"Segunda palabra: {segunda_palabra}") """


######### 3° Solución: un solo bucle, tomando de a pares #########

palabra_intercalada: str = "hcohlaau"

primer_palabra: str = str()
segunda_palabra: str = str()

for i in range(len(palabra_intercalada) // 2):
    primer_palabra += palabra_intercalada[i * 2]
    segunda_palabra += palabra_intercalada[i * 2 + 1]

print(f"Primer palabra: {primer_palabra}")
print(f"Segunda palabra: {segunda_palabra}")
