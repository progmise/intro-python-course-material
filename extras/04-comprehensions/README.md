# Extra 04: List y Dict Comprehensions

## 📌 Descripción
Ejemplos de creación de colecciones por comprensión:

- **List comprehension**: obtener los nombres de los alumnos con nota mayor a 7.
- **Dict comprehension**: construir un diccionario a partir de una lista de tuplas `(llave, valor)`, filtrando por llave.

Cada ejemplo incluye, comentado, el equivalente manual con bucle `for`.

## 🧠 Conceptos Aplicados
- Sintaxis de *list comprehension* con filtro: `[expresion for item in iterable if condicion]`.
- Sintaxis de *dict comprehension*: `{llave: valor for llave, valor in iterable if condicion}`.
- Desempaquetado de tuplas en el `for` de una comprehension.

## 📥 Ejemplo de Entrada / Salida
- No requiere entrada.
  - **Salida**: `['Nicolas', 'Nicolas']` y `{3: 'Amarillo'}`

## 🚀 Cómo ejecutar
```bash
python main.py
```
