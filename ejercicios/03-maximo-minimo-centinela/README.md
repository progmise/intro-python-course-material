# Ejercicio 03: Máximo y Mínimo con Centinela

## 📌 Enunciado
Solicitar el ingreso de `n` números enteros, uno por vez, hasta que el usuario ingrese `*` (centinela). Al finalizar, mostrar el **máximo** y el **mínimo** de los valores cargados.

## 🧠 Conceptos Aplicados
- Bucle `while` con condición de corte (valor centinela).
- Inicialización del máximo/mínimo con el **primer valor ingresado** (no con un número arbitrario).
- Bandera booleana para detectar si hubo ingresos.
- Comparaciones y actualización de acumuladores de extremos.

## 📥 Ejemplo de Entrada / Salida
- **Entrada**: `4`, `9`, `-2`, `7`, `*`
  - **Salida**: `El número máximo es: 9` / `El número mínimo es: -2`
- **Entrada**: `*` (sin números)
  - **Salida**: `No se ingresaron números.`

## 🚀 Cómo ejecutar
```bash
python main.py
```
