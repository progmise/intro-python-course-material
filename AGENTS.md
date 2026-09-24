# AGENTS.md - Directrices para Asistentes y Agentes de IA

Este documento establece los estándares, la arquitectura del repositorio y las pautas de desarrollo que cualquier agente de IA o desarrollador debe respetar al interactuar con **intro-python-course-material**.

---

## 📌 Contexto y Propósito del Repositorio

**intro-python-course-material** es un repositorio educativo con ejercicios de programación, ejemplos de buenas prácticas y casos de estudio de refactorización en Python para un curso introductorio en **FIUBA**. Su propósito es ofrecer soluciones limpias, didácticas, autoexplicativas y bien documentadas.

---

## 📂 Arquitectura y Organización del Proyecto

El repositorio sigue un esquema estrictamente **modular**:

```text
intro-python-course-material/
├── README.md                  # Índice global y catálogo temático
├── AGENTS.md                  # Reglas y directrices del repositorio
├── ejercicios/
│   ├── 01-operaciones-basicas/
│   │   ├── README.md          # Enunciado, conceptos, ejemplos I/O y ejecución
│   │   └── main.py            # Código fuente documentado
│   └── ...
├── buenas-practicas/
│   └── 01-indentacion-pep8/   # Misma estructura: README.md + main.py
├── codigo-repetido/
│   └── 01-algoritmo-para-quitar-codigo-repetido/  # Puede ser solo README.md
└── extras/
    └── 01-consumo-api/        # Material misceláneo que no encaja en otra sección
```

### Reglas de Organización:
1. **Prohibido crear archivos `.py` sueltos en la raíz**: todo nuevo código debe ubicarse dentro de su correspondiente subcarpeta en `ejercicios/`, `buenas-practicas/`, `codigo-repetido/` o `extras/` (material misceláneo que no encaja en las demás secciones).
2. **Autocontenido**: cada carpeta debe ser autónoma y contener su propio `README.md` explicativo. Si requiere recursos (imágenes, datasets), deben convivir dentro de la misma carpeta.
3. **Numeración correlativa**: las carpetas se nombran `NN-nombre-descriptivo` en minúsculas con guiones.
4. **Actualización del Catálogo Central**: cada vez que se agregue o renombre un material, se debe actualizar la tabla de contenidos del [`README.md`](README.md) principal.
5. **Secretos**: nunca hardcodear credenciales ni API keys; usar variables de entorno.

---

## 🐍 Convenciones y Estándares de Código (PEP 8)

### 1. Nomenclatura:
- **`snake_case` estricto**: variables, funciones, métodos y archivos `.py` en minúsculas con guiones bajos (e.g., `cantidad_de_alumnos`, `calcular_promedio`).
- **Nombres declarativos y autoexplicativos**: evitar abreviaciones crípticas.
- **Constantes**: `UPPER_SNAKE_CASE` (e.g., `CANTIDAD_DE_FILAS`).

### 2. Estructura de cada `main.py`:
- Cabecera con docstring explicativo (`""" Ejercicio XX: ... """`).
- Declaración de funciones modulares con responsabilidades únicas.
- Lectura de datos limpia con mensajes descriptivos al usuario.
- Manejo de rutas mediante `pathlib.Path` para recursos locales:
  ```python
  from pathlib import Path
  RUTA_IMAGEN = Path(__file__).parent / "imagenes" / "archivo.jpg"
  ```

### 3. Estructura de cada `README.md` por carpeta:
- `# Ejercicio/Material XX: [Título Descriptivo]`
- `## 📌 Enunciado` (o `## 📌 Descripción`): explicación del problema o tema.
- `## 🧠 Conceptos Aplicados`: lista de herramientas y estructuras utilizadas.
- `## 📥 Ejemplo de Entrada / Salida`: muestras claras de ejecución (si aplica).
- `## 🚀 Cómo ejecutar`: comando de consola para probar el archivo.

### 4. Excepción didáctica:
El material de `codigo-repetido/` conserva a propósito el código "antes de refactorizar" como caso de estudio: no aplicar mejoras de estilo ni reestructuración a menos que se pida explícitamente una versión refactorizada.

---

## 🤖 Skills Disponibles

El repositorio incluye skills de workflow en `.agents/skills/`:

- **`python-exercise-creator`**: crear e integrar un nuevo material (carpeta, `main.py`, `README.md`, catálogo central).
- **`pep8-quality-auditor`**: auditar nomenclatura, estructura, rutas y READMEs de todo el repo.
- **`python-exercise-tester`**: generar y ejecutar tests `unittest` sobre los ejercicios.

---

## 🛠️ Comandos de Validación Frecuentes

Antes de dar por completada cualquier tarea:

- **Validación de sintaxis de todos los archivos**:
  ```bash
  python -m compileall ejercicios/ buenas-practicas/ codigo-repetido/ extras/
  ```
- **Ejecución de un ejercicio específico**:
  ```bash
  python ejercicios/01-operaciones-basicas/main.py
  ```
