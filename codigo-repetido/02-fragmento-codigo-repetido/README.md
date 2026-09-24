# Código Repetido 02: Fragmento con Código Duplicado (Antes)

## 📌 Descripción
Fragmento de la función `cargar_palabras` del juego de crucigrama, conservado **a propósito sin refactorizar** como material de análisis para la clase de eliminación de código duplicado.

⚠️ **No es ejecutable**: es un fragmento con referencias externas (`randint`, `tablero`, `lista_de_filas`, etc.). Para ver el contexto completo, ir a [`03-crucigrama`](../03-crucigrama/).

## 🧠 Qué observar
- La función recibe **12 parámetros**: señal de que fue creada copiando bloques repetidos y parametrizando lo que cambiaba.
- Dos llamadas con distintos rangos (verticales vs. horizontales) comparten la misma lógica.
- Ejercicio sugerido: aplicar el algoritmo de [`01-algoritmo-para-quitar-codigo-repetido`](../01-algoritmo-para-quitar-codigo-repetido/) para reducir la firma y la duplicación restante en `crucigrama.py`.

## 🚀 Cómo ejecutar
No ejecutable. Compila sintácticamente pero falla en tiempo de ejecución por las referencias externas.
