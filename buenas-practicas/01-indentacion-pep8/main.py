"""
Buenas prácticas 01: Indentación según PEP 8.

Ejemplos correctos e incorrectos de indentación en firmas de funciones,
llamadas multilínea, estructuras if y delimitadores de cierre.

Referencia: https://peps.python.org/pep-0008/
"""

variable_uno: str = str()
variable_dos: str = str()
variable_tres: str = str()
variable_cuatro: str = str()
esto_es_una_cosa: bool = bool()
esto_es_otra_cosa: bool = bool()


def hacer_algo() -> None:
    pass


def una_funcion_con_muchos_argumentos(a, b, c, d, e, f) -> None:
    pass


# FIRMA DE FUNCIONES Y LLAMADO DE FUNCIONES
# Se debe usar 4 espacios por nivel de indentación

# Correcto:

# Se agregan 4 espacios (un nivel extra de indentación) para distinguir los argumentos, del resto del cuerpo de la función
def una_funcion_larga(
        variable_uno, variable_dos, variable_tres,
        variable_cuatro):
    print(variable_uno)

# Alineado con delimitador abierto
foo = una_funcion_larga(variable_uno, variable_dos,
                        variable_tres, variable_cuatro)

# Sin alineación de delimitador abierto, pero con un nivel de indentación
foo = una_funcion_larga(
    variable_uno, variable_dos,
    variable_tres, variable_cuatro)


# Incorrecto:

# Los argumentos de la primera línea se pierden, al no usar alineación vertical
foo = una_funcion_larga(variable_uno, variable_dos,
    variable_tres, variable_cuatro)

# Se precisa una indentación adicional, ya que no se logra distinguir el cuerpo de la función, de los argumentos
def una_funcion_larga(
    variable_uno, variable_dos, variable_tres,
    variable_cuatro):
    print(variable_uno)


# Opcional:

# Al manejar la indentación, se puede obviar la regla de los 4 espacios
foo = una_funcion_larga(
  variable_uno, variable_dos,
  variable_tres, variable_cuatro)


# ESTRUCTURA IF

# Sin indentación extra
if (esto_es_una_cosa and
    esto_es_otra_cosa):
    hacer_algo()

# Agregar un comentario, proporciona cierta distinción en los IDE's
if (esto_es_una_cosa and
    esto_es_otra_cosa):
    # Un comentario
    hacer_algo()

# Se puede agregar una indentación adicional en la linea de continación condicional
if (esto_es_una_cosa
        and esto_es_otra_cosa):
    hacer_algo()


# PARENTESIS/CORCHETE/LLAVE DE CIERRE

# Puede estar alineado con el mismo nivel de indentación de los argumentos
mi_lista = [
    1, 2, 3,
    4, 5, 6
    ]

resultado = una_funcion_con_muchos_argumentos(
    'a', 'b', 'c',
    'd', 'e', 'f'
    )


# O bien, puede estar debajo del primer carácter de la linea que inicia la estructura multilinea

mi_lista = [
    1, 2, 3,
    4, 5, 6
]

resultado = una_funcion_con_muchos_argumentos(
    'a', 'b', 'c',
    'd', 'e', 'f'
)
