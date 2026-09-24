# Extra 03: GUI con tkinter + Pillow

## 📌 Descripción
Ejemplo de interfaz gráfica: una grilla de 3x3 `Frame`s que simula el mapa de un juego RPG, con una imagen cargada en la celda superior izquierda.

Mejoras respecto a la versión original de clase:

- Importaciones explícitas (`import tkinter as tk`) en lugar de `from tkinter import *`.
- `Image.Resampling.LANCZOS` en lugar de `Image.ANTIALIAS` (eliminado en Pillow 10+).
- La ruta de la imagen se resuelve con `pathlib.Path` relativa al archivo, para que funcione desde cualquier directorio.

## 🧠 Conceptos Aplicados
- `tkinter`: `Tk`, `Frame`, `Label`, layout con `.grid()`.
- `Pillow` (`PIL`): `Image.open()`, `resize()` con filtro `LANCZOS`, `ImageTk.PhotoImage`.
- `pathlib.Path` para rutas relativas al script.
- Clases como contenedor de la vista (`GameScreen`).

## 📦 Requisitos
```bash
pip install pillow
```

## 🚀 Cómo ejecutar
```bash
python main.py
```

Las imágenes de ejemplo están en `imagenes/`.
