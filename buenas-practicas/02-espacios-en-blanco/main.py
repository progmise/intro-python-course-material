"""
Buenas prácticas 02: Espacios en blanco dentro del código.

Ejercicio "two-sum" con gustos de helado: dada una lista de tuplas
(gusto, precio) y un presupuesto k, devolver el par de gustos cuyos
precios suman exactamente k.

Primero se muestra la versión con indentación irregular (INCORRECTA,
comentada) y luego la misma función bien formateada (CORRECTA).
"""


######### INCORRECTO: indentación irregular #########

# def comprar_palitos_de_helado(palitos: list, k: int) -> dict:
#     vistos: dict = dict()
#
#     for i in range(len(palitos)):
#       helado, precio = palitos[i]
#       aux: int = k - precio
#
#       if aux in vistos:
#         return { aux: vistos[aux], helado: precio }
#       else:
#         vistos[precio] = helado


######### CORRECTO: 4 espacios por nivel #########

def comprar_palitos_de_helado(palitos: list, k: int) -> dict:
    vistos: dict = dict()

    for helado, precio in palitos:
        aux: int = k - precio

        if aux in vistos:
            return {aux: vistos[aux], helado: precio}
        else:
            vistos[precio] = helado


print(comprar_palitos_de_helado([("Frutilla", 200), ("Chocolate", 150), ("Durazno", 100), ("Manzana", 400)], 250))
