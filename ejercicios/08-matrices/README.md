# Ejercicio 08: Matrices (Listas de Listas)

## 📌 Enunciado
Demostración de tres temas sobre matrices en Python:

1. **Recorrido** de una matriz por índices (`range(len(...))`) y por elementos (`for fila in matriz`).
2. **El error clásico** `[[0] * columnas] * filas`: todas las filas referencian a la *misma* lista, por lo que modificar una celda "contamina" a todas las filas.
3. **Creación correcta** con bucles anidados (o list comprehension).

## 🧠 Conceptos Aplicados
- Matrices como listas de listas.
- Aliasing: referencias compartidas al multiplicar listas.
- Bucles anidados para construir estructuras bidimensionales.
- List comprehension como alternativa segura: `[[0] * columnas for _ in range(filas)]`.

## 📥 Ejemplo de Entrada / Salida
No requiere entrada. Al ejecutar se observa que en la matriz incorrecta el valor `3` aparece en la primera columna de **todas** las filas, mientras que en la correcta solo cambia `matriz[0][0]`.

## 🚀 Cómo ejecutar
```bash
python main.py
```
