"""
Buenas prácticas 03: Otras recomendaciones de PEP 8.

Espacios alrededor de operadores, typing, argumentos por palabra clave
y declaraciones compuestas: ejemplos correctos e incorrectos.

Referencia: https://peps.python.org/pep-0008/
"""

i: int = int()
contador: int = int()
x: int = int()
y: int = int()
a: int = int()
b: int = int()
t: int = int()
foo: str = str()
lst: list = list()
total: int = int()
lista: str = str()
argumentos: str = str()
largos: str = str()
como: str = str()
este: str = str()


def magia(r, i): ...


def hacer_algo_blah(): ...


def hacer_no_algo_blah(): ...


def hacer_algo_uno(): ...


def hacer_algo_dos(): ...


def hacer_algo_tres(*args): ...


def retraso() -> int:
    return 10


def algo(): ...


def limpiar(): ...


# Evitar los espacios en blanco finales en cualquier lugar. Debido a que generalmente es invisible, puede ser confuso.

# Siempre rodear los operadores binarios con un solo espacio a cada lado: asignación (=), aumento y asignación (+=, -= etc.), comparación (==, <, >, !=, <>, <=, >=, in, not in, is, is not), Booleans (and, or, not).

# Si se utilizan operadores con diferentes prioridades, se debe agregar espacios en blanco alrededor de los operadores con la(s) prioridad(es) más baja(s).

# Correcto:
i = i + 1

contador += 1

x = x*2 - 1

hypot2 = x*x + y*y

c = (a+b) * (a-b)

# Incorrecto:
i=i+1

contador +=1

x = x * 2 - 1

hypot2 = x * x + y * y

c = (a + b) * (a - b)


# El typing debe usar las reglas normales para los dos puntos y siempre tener espacios alrededor de la flecha.

# Correcto:
def una_funcion(input: str): ...

def una_funcion() -> int: ...

# Incorrecto:
def una_funcion(input:str): ...

def una_funcion()->int: ...


# No usar espacios alrededor del signo = cuando se usa para indicar un argumento de palabra clave, o cuando se usa para indicar un valor predeterminado para un parámetro de una función:

# Correcto:

def complex(real, imag=0.0):
    return magia(r=real, i=imag)

# Incorrecto:
def complex(real, imag = 0.0):
    return magia(r = real, i = imag)


# Al combinar typing con un valor predeterminado, se debe utilizar espacios alrededor del signo = :

# Correcto:
def una_funcion(sep: str = None): ...

def una_funcion(input: str, sep: str = None, limit=1000): ...

# Incorrecto:
def una_funcion(input: str=None): ...

def una_funcion(input: str, limit = 1000): ...


# No se recomiendan las declaraciones compuestas:

# Correcto:
if foo == 'blah':
    hacer_algo_blah()
hacer_algo_uno()
hacer_algo_dos()
hacer_algo_tres()

# Incorrecto:
if foo == 'blah': hacer_algo_blah()
hacer_algo_uno(); hacer_algo_dos(); hacer_algo_tres()


# Si bien a veces está bien poner un if/for/while con un cuerpo pequeño en la misma línea, nunca se debe hacer esto para declaraciones de varias cláusulas.

# Incorrecto:
if foo == 'blah': hacer_algo_blah()
for x in lst: total += x
while t < 10: t = retraso()


# Definitivamente no:

# Incorrecto:
if foo == 'blah': hacer_algo_blah()
else: hacer_no_algo_blah()

try: algo()
finally: limpiar()

hacer_algo_uno(); hacer_algo_dos(); hacer_algo_tres(lista, argumentos,
                                                    largos, como, este)

if foo == 'blah': hacer_algo_uno(); hacer_algo_dos(); hacer_algo_tres()
