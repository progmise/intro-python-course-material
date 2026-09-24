---
name: python-exercise-creator
description: >-
  Workflow para crear e integrar un nuevo material de práctica en intro-python-course-material.
  Crea la carpeta dedicada bajo la sección correspondiente (ejercicios/, buenas-practicas/, extras/),
  el archivo main.py con nombres declarativos en snake_case, el README.md local estructurado
  y actualiza el catálogo del README.md central.
---

# Skill: Python Exercise Creator

Esta skill define el procedimiento paso a paso para agregar un nuevo material al repositorio
**intro-python-course-material**, asegurando la coherencia arquitectónica, los estándares de código
y la documentación requerida.

---

## 📋 Flujo de Trabajo

### Paso 1: Determinar la Sección, Numeración y Slug
1. Elegir la sección según el tipo de material:
   - `ejercicios/`: problemas con enunciado que el alumno debe resolver.
   - `buenas-practicas/`: ejemplos de estilo y convenciones (PEP 8).
   - `extras/`: demos de referencia, programas completos y material misceláneo.
   - `codigo-repetido/`: solo casos de estudio de refactorización (material "antes").
2. Listar la sección elegida para identificar el último número utilizado.
3. Definir el siguiente número correlativo de dos dígitos (`XX`).
4. Definir un slug en `kebab-case` descriptivo (ejemplo: `12-calculo-factorial`).
5. La carpeta destino será: `<seccion>/XX-slug-descriptivo/`.

### Paso 2: Crear el archivo `main.py`
El código fuente debe cumplir estrictamente con los siguientes lineamientos:
- **Cabecera**: Docstring breve con el número y objetivo:
  ```python
  """
  Ejercicio XX: [Descripción clara del objetivo].
  """
  ```
  (Usar `Material XX:` o `Extra XX:` según la sección.)
- **Nomenclatura**: `snake_case` estricto para todas las variables y funciones.
- **Nombres declarativos**: Evitar abreviaciones (usar `numero_ingresado`, `total_acumulado`).
- **Modularidad**: Si el ejercicio requiere lógica reutilizable, declararla en funciones con responsabilidad única.
- **Recursos locales**: Rutas con `pathlib.Path` relativas al archivo (`Path(__file__).parent / ...`).
- **Secretos**: Nunca hardcodear credenciales; leer variables de entorno con `os.environ.get()`.

### Paso 3: Crear el archivo `README.md` del Material
Cada carpeta debe contar con su documentación local usando la siguiente plantilla estándar:

````markdown
# Ejercicio XX: [Título Descriptivo]

## 📌 Enunciado
[Explicación formal, clara y pedagógica del problema a resolver, incluyendo fórmulas si aplica.
Para material de referencia usar `## 📌 Descripción` en su lugar.]

## 🧠 Conceptos Aplicados
- [Concepto 1: e.g. Estructuras condicionales if / elif / else]
- [Concepto 2: e.g. Módulo estándar math]
- [Concepto 3: e.g. Manejo de listas y métodos de strings]

## 📥 Ejemplo de Entrada / Salida
- **Entrada**: `[Valores de prueba]`
  - **Salida**: `[Salida esperada formateada]`

## 🚀 Cómo ejecutar
```bash
python main.py
```
````

### Paso 4: Actualizar el Catálogo en el `README.md` Raíz
1. Abrir [`README.md`](../../../README.md).
2. Ubicar la tabla de la sección correspondiente (o crear una subsección temática si es un tema nuevo).
3. Agregar la fila con el número, título, conceptos y enlace directo:
   ```markdown
   | **XX** | **[Título]** | [Conceptos clave] | [Ver Ejercicio](ejercicios/XX-slug-descriptivo/) |
   ```
4. Actualizar también el bloque `Estructura General del Repositorio` del mismo README.

### Paso 5: Validación
Ejecutar la validación de compilación para descartar errores de sintaxis:
```bash
python -m compileall <seccion>/XX-slug-descriptivo/
```
