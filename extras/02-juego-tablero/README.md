# Extra 02: Juego de Tablero para Dos Jugadores

## 📌 Descripción
Juego por turnos sobre un tablero de 4x4: al primer jugador se le asignan los `1` y al segundo los `2`. En cada turno se puede:

- `a` / `d` / `w` / `s`: desplazar las piezas propias una celda (izquierda, derecha, arriba, abajo) hacia celdas `0`.
- `r`: rotar el tablero 90° en sentido horario.
- `t`: reflejar el tablero sobre el eje vertical.

La partida dura 10 rondas. Es un ejemplo de modularización con funciones y dispatch por opción.

## 🧠 Conceptos Aplicados
- Matrices y recorridos por filas y columnas.
- Intercambio de valores con asignación múltiple (`a, b = b, a`).
- Rotación de matriz con `zip(*tablero[::-1])` y reflexión con `.reverse()`.
- Dispatch de opciones con `if/elif` y funciones modulares.
- `random.randint()` para el sorteo inicial.

## 🚀 Cómo ejecutar
```bash
python main.py
```
