"""
Extra 03: GUI con tkinter + Pillow.

Ejemplo de interfaz gráfica: una grilla de 3x3 Frames que simula el
mapa de un juego RPG, con una imagen cargada en la celda superior
izquierda.

Requiere: pip install pillow
Las imágenes se leen desde la carpeta imagenes/ junto a este archivo.
"""

from pathlib import Path
import tkinter as tk

from PIL import Image, ImageTk

RUTA_IMAGEN: Path = Path(__file__).parent / "imagenes" / "napoleon.jpg"


class GameScreen:
    def __init__(self, master: tk.Tk) -> None:
        # Se crean todos los contenedores principales
        top_left = tk.Frame(master, bg='black', width=200, height=200)
        top_middle = tk.Frame(master, bg='green', width=200, height=200)
        top_right = tk.Frame(master, bg="green", width=200, height=200)
        middle_left = tk.Frame(master, bg='green', width=200, height=200)
        middle = tk.Frame(master, bg='green', width=200, height=200)
        middle_right = tk.Frame(master, bg='green', width=200, height=200)
        bottom_left = tk.Frame(master, bg='green', width=200, height=200)
        bottom_middle = tk.Frame(master, bg='green', width=200, height=200)
        bottom_right = tk.Frame(master, bg='green', width=200, height=200)

        # Se ubican los contenedores en la grilla
        top_left.grid(row=0, column=0, padx=0, pady=0)
        top_middle.grid(row=0, column=1)
        top_right.grid(row=0, column=2)
        middle_left.grid(row=1, column=0)
        middle.grid(row=1, column=1)
        middle_right.grid(row=1, column=2)
        bottom_left.grid(row=2, column=0)
        bottom_middle.grid(row=2, column=1)
        bottom_right.grid(row=2, column=2)

        image = Image.open(RUTA_IMAGEN)
        photo = ImageTk.PhotoImage(image.resize((196, 196), Image.Resampling.LANCZOS))

        label = tk.Label(top_left, image=photo, bg='green')
        label.image = photo
        label.pack()


def main() -> None:
    root = tk.Tk()
    root.title("RPG Game")
    root.geometry("600x600")
    GameScreen(root)
    root.mainloop()


main()
