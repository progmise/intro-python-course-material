# Código Repetido 03: Crucigrama (Antes de Refactorizar)

## 📌 Descripción
Juego de crucigrama completo (trabajo práctico de alumnos) conservado **sin refactorizar**: es el caso de estudio principal para la clase de eliminación de código duplicado.

**Reglas del juego**: hay que descubrir 12 palabras (6 horizontales y 6 verticales) elegidas al azar. Cada palabra está referenciada con una letra (A a L) y debajo del tablero se listan las definiciones. Si se erra una respuesta, se tira un dado:

- `1` o `2`: una palabra ya acertada se reemplaza por una nueva.
- `3` o `4`: se revelan todas las vocales en el tablero.
- `5`: se puede elegir una definición para revelar su palabra automáticamente.
- `6`: *dado de la muerte*, se pierde el juego.

## 🧠 Qué observar (ejercicio de refactorización)
- Funciones con más de 10 parámetros (`cargar_palabras`, `verificar_respuesta_usuario`).
- Bloques casi idénticos para palabras verticales y horizontales.
- `dado_uno_o_dos`, `dado_tres_o_cuatro`, `actualizar_tablero`: candidatas a aplicar el algoritmo de [`01-algoritmo-para-quitar-codigo-repetido`](../01-algoritmo-para-quitar-codigo-repetido/).
- Estado global implícito pasado por listas: oportunidad para encapsular.

## ⚠️ Notas
- Usa `os.system("cls")`: pensado para consola de Windows.

## 🚀 Cómo ejecutar
```bash
python main.py
```
