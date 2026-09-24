# Ejercicio 07: Menú de Alumnos con Listas Paralelas

## 📌 Enunciado
Crear un programa que permita al usuario elegir entre las siguientes opciones:

1. **Agregar un alumno**: se solicitan nombre, padrón y nota.
2. **Consultar aprobados**: mostrar los alumnos con nota mayor o igual a 4.
3. **Cantidad de alumnos totales y promedio general**.
4. **Quitar a un alumno** por su padrón.
5. **Salir**.

La información se almacena en **tres listas paralelas** (`nombres`, `padrones`, `notas`) donde el índice `i` identifica al mismo alumno en las tres.

## 🧠 Conceptos Aplicados
- Listas paralelas como estructura de datos.
- Menú interactivo con `while` centinela y dispatch con `if/elif`.
- Modularización del programa en funciones con responsabilidad única.
- Métodos de lista: `.append()`, `.pop()`, `.index()`; verificación con `in`.
- Funciones built-in `len()`, `sum()` y formateo con `:.2f`.

## 📥 Ejemplo de Entrada / Salida
- **Entrada**: opción `1` → nombre `Ana`, padrón `105123`, nota `7` → `N`; luego opción `3` y `5`
  - **Salida**: `Cantidad de alumnos: 1` / `Promedio general: 7.00`

## 🚀 Cómo ejecutar
```bash
python main.py
```
