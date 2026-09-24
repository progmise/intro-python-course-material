"""
Ejercicio 01: Operaciones básicas y formatos de impresión.

Implementar un programa que pida al usuario que ingrese dos números
y muestre la suma, resta, multiplicación y división de ambos.

Se muestran 5 variantes para formatear la salida por consola.
"""

primer_numero: int = int(input("Ingrese un número: "))
segundo_numero: int = int(input("Ingrese otro número: "))

suma: int = primer_numero + segundo_numero

# Variante 1: método str.format()
print("La suma de los números {0} y {1} es {2}".format(primer_numero, segundo_numero, suma))

# Variante 2: múltiples argumentos de print()
print("La suma de los números", primer_numero, "y", segundo_numero, "es", suma)

# Variante 3: concatenación de cadenas
print("La suma de los números " + str(primer_numero) + " y " + str(segundo_numero) + " es " + str(suma))

# Variante 4: operador % (estilo heredado de C)
print("La suma de los números %s y %s es %s" % (primer_numero, segundo_numero, suma))

# Variante 5: f-string (forma recomendada desde Python 3.6)
print(f"La suma de los números {primer_numero} y {segundo_numero} es {suma}")

print(f"La resta de los números {primer_numero} y {segundo_numero} es {primer_numero - segundo_numero}")
print(f"La multiplicación de los números {primer_numero} y {segundo_numero} es {primer_numero * segundo_numero}")
print(f"La división de los números {primer_numero} y {segundo_numero} es {primer_numero / segundo_numero}")
