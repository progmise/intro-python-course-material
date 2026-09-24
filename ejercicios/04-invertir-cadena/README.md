# Ejercicio 04: Invertir una Cadena

## 📌 Enunciado
Pedir al usuario que ingrese una cadena de caracteres. El programa debe **invertir** esa cadena y mostrarla por consola.

Se presentan 3 soluciones: slicing con paso negativo, `list.reverse()` + `str.join()`, y recorrido manual con `range()` descendente.

## 🧠 Conceptos Aplicados
- Slicing de cadenas con paso (`[::-1]`).
- Conversión cadena ↔ lista, métodos `.reverse()` y `.join()`.
- `range(inicio, fin, paso)` con paso negativo para recorrer índices de atrás hacia adelante.
- Concatenación de caracteres en un bucle `for`.

## 📥 Ejemplo de Entrada / Salida
- **Entrada**: `hola`
  - **Salida**: `Palabra modificada: 'aloh'`

## 🚀 Cómo ejecutar
```bash
python main.py
```

Para probar las otras soluciones, descomentar el bloque correspondiente y comentar la solución activa.
