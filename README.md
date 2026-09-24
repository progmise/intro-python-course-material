# Intro Python Course Material - FIUBA 🐍

Material de clase para un curso introductorio de programación en Python (**FIUBA**): ejercicios prácticos, ejemplos de buenas prácticas (PEP 8), casos de estudio sobre código repetido y refactorización, y material extra misceláneo.

Cada tema está organizado de forma modular en su propio directorio, con el código fuente en `main.py` y un `README.md` que detalla el enunciado, los conceptos aplicados y ejemplos de entrada/salida.

---

## 📂 Estructura General del Repositorio

```text
intro-python-course-material/
├── README.md
├── ejercicios/
│   ├── 01-operaciones-basicas/
│   ├── 02-decisiones/
│   ├── 03-maximo-minimo-centinela/
│   ├── 04-invertir-cadena/
│   ├── 05-palabras-intercaladas/
│   ├── 06-maximo-minimo-lista/
│   ├── 07-menu-alumnos/
│   ├── 08-matrices/
│   ├── 09-menu-paises/
│   ├── 10-conjuntos-promedios/
│   └── 11-tablero-pieza/
├── buenas-practicas/
│   ├── 01-indentacion-pep8/
│   ├── 02-espacios-en-blanco/
│   └── 03-recomendaciones-pep8/
├── codigo-repetido/
│   ├── 01-algoritmo-para-quitar-codigo-repetido/
│   ├── 02-fragmento-codigo-repetido/
│   └── 03-crucigrama/
└── extras/
    ├── 01-consumo-api/
    ├── 02-juego-tablero/
    ├── 03-gui-tkinter/
    ├── 04-comprehensions/
    └── 05-ordenamiento-filtrado/
```

---

## 📚 Índice de Ejercicios Prácticos

### 1️⃣ Entrada/Salida, Aritmética y Decisiones
| # | Ejercicio | Conceptos | Enlace |
| :-: | :--- | :--- | :-: |
| **01** | **Operaciones Básicas** | `input()`, operadores, 5 formas de formatear salida | [Ver Ejercicio](ejercicios/01-operaciones-basicas/) |
| **02** | **Estructuras de Decisión** | `if/elif/else`, mutación dentro de ramas | [Ver Ejercicio](ejercicios/02-decisiones/) |

### 2️⃣ Bucles y Cadenas
| # | Ejercicio | Conceptos | Enlace |
| :-: | :--- | :--- | :-: |
| **03** | **Máximo y Mínimo con Centinela** | `while`, valor centinela, banderas | [Ver Ejercicio](ejercicios/03-maximo-minimo-centinela/) |
| **04** | **Invertir una Cadena** | Slicing `[::-1]`, `.reverse()`, `range()` descendente | [Ver Ejercicio](ejercicios/04-invertir-cadena/) |
| **05** | **Palabras Intercaladas** | Slicing con paso, índices pares/impares | [Ver Ejercicio](ejercicios/05-palabras-intercaladas/) |

### 3️⃣ Listas, Matrices y Menús
| # | Ejercicio | Conceptos | Enlace |
| :-: | :--- | :--- | :-: |
| **06** | **Máximo y Mínimo de una Lista** | `max()`/`min()`, recorrido manual, funciones | [Ver Ejercicio](ejercicios/06-maximo-minimo-lista/) |
| **07** | **Menú de Alumnos** | Listas paralelas, menú interactivo, CRUD | [Ver Ejercicio](ejercicios/07-menu-alumnos/) |
| **08** | **Matrices** | Aliasing, creación correcta, recorridos | [Ver Ejercicio](ejercicios/08-matrices/) |
| **09** | **Menú de Países** | Listas de listas, filtrado, estadísticas | [Ver Ejercicio](ejercicios/09-menu-paises/) |
| **10** | **Conjuntos y Promedios** | `set`, diccionarios, contadores y acumuladores | [Ver Ejercicio](ejercicios/10-conjuntos-promedios/) |
| **11** | **Tablero y Pieza** | Matrices, desempaquetado de coordenadas | [Ver Ejercicio](ejercicios/11-tablero-pieza/) |

---

## ✨ Buenas Prácticas (PEP 8 y Estilo)

| # | Material | Conceptos | Enlace |
| :-: | :--- | :--- | :-: |
| **01** | **Indentación PEP 8** | 4 espacios, argumentos multilínea, delimitadores | [Ver Material](buenas-practicas/01-indentacion-pep8/) |
| **02** | **Espacios en Blanco** | Indentación consistente, diccionario de "vistos" | [Ver Material](buenas-practicas/02-espacios-en-blanco/) |
| **03** | **Recomendaciones PEP 8** | Operadores, typing, `=` en kwargs, una sentencia por línea | [Ver Material](buenas-practicas/03-recomendaciones-pep8/) |

---

## ♻️ Código Repetido y Refactorización

| # | Material | Conceptos | Enlace |
| :-: | :--- | :--- | :-: |
| **01** | **Algoritmo para Quitar Código Repetido** | DRY, parametrización, abstracción | [Ver Material](codigo-repetido/01-algoritmo-para-quitar-codigo-repetido/) |
| **02** | **Fragmento con Código Repetido** | Firma de 12 parámetros, análisis (no ejecutable) | [Ver Material](codigo-repetido/02-fragmento-codigo-repetido/) |
| **03** | **Crucigrama** | Caso de estudio completo para refactorizar | [Ver Material](codigo-repetido/03-crucigrama/) |

---

## 📎 Extras

| # | Material | Conceptos | Enlace |
| :-: | :--- | :--- | :-: |
| **01** | **Consumo de API REST** | `requests`, headers, API key por variable de entorno | [Ver Material](extras/01-consumo-api/) |
| **02** | **Juego de Tablero** | Modularización, dispatch de opciones, rotación de matrices | [Ver Material](extras/02-juego-tablero/) |
| **03** | **GUI con tkinter** | `tkinter`, `Pillow`, `pathlib` | [Ver Material](extras/03-gui-tkinter/) |
| **04** | **Comprehensions** | List/dict comprehension con filtros | [Ver Material](extras/04-comprehensions/) |
| **05** | **Ordenamiento y Filtrado** | `lambda`, `.sort()`/`sorted()`, `filter()` | [Ver Material](extras/05-ordenamiento-filtrado/) |

---

## 🚀 Requisitos y Ejecución

- **Python 3.8+** (la mayoría del material no requiere librerías externas).
- Excepciones:
  - `extras/03-gui-tkinter`: `pip install pillow`
  - `extras/01-consumo-api`: `pip install requests` + variable de entorno `API_SPORTS_KEY`
- Para ejecutar cualquier ejercicio:
  ```bash
  cd ejercicios/01-operaciones-basicas
  python main.py
  ```
