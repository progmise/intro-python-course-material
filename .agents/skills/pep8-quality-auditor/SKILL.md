---
name: pep8-quality-auditor
description: >-
  Workflow para auditar la calidad y el estilo de código de todo el repositorio.
  Verifica nomenclatura snake_case, nombres declarativos, importaciones, uso de pathlib
  para rutas de recursos, y ejecuta compileall para validar sintaxis.
  NO audita codigo-repetido/, que conserva código "antes de refactorizar" a propósito.
---

# Skill: PEP 8 Quality Auditor

Esta skill define el procedimiento completo para realizar una auditoría de calidad sobre el código
del repositorio **intro-python-course-material**, asegurando que todos los archivos cumplan con los
estándares de estilo PEP 8 y las convenciones propias del proyecto documentadas en
[`AGENTS.md`](../../../AGENTS.md).

---

## 📋 Flujo de Trabajo

### Paso 0: Alcance de la Auditoría

- ✅ Auditar: `ejercicios/`, `buenas-practicas/`, `extras/`.
- ❌ **NO auditar**: `codigo-repetido/` — conserva a propósito el código "antes de refactorizar"
  como caso de estudio didáctico. Sus violaciones de estilo son intencionales.

### Paso 1: Auditoría de Nomenclatura

Recorrer todos los archivos `.py` de las secciones auditables verificando:

#### Variables y Funciones
- ✅ **`snake_case` estricto**: Todas las variables, funciones y parámetros en minúsculas con guiones bajos.
  - Correcto: `numero_ingresado`, `es_anio_bisiesto`, `calcular_promedio`
  - Incorrecto: `capitalTotal`, `esAnioBisiesto`, `primerCoef`
- ✅ **Nombres declarativos y autoexplicativos**: Cada identificador debe comunicar su propósito sin ambigüedad.
  - Correcto: `horas_primer_horario`, `cantidad_aprobados`, `lista_numeros_positivos`
  - Incorrecto: `hs1`, `cant_ap`, `l` (salvo en `for i in range()`)

#### Constantes
- ✅ **`UPPER_SNAKE_CASE`**: Para valores inmutables y rutas de archivo.
  - Ejemplo: `CANTIDAD_DE_FILAS`, `RUTA_IMAGEN`, `NOTA_APROBACION`

#### Funciones
- ✅ Los nombres deben comenzar con un verbo indicativo de acción:
  - Correcto: `calcular_`, `es_`, `obtener_`, `mostrar_`, `cargar_`, `contar_`
  - Incorrecto: `resultado()`, `datos()`, `proceso()`

### Paso 2: Auditoría de Estructura de Archivos

Para cada `main.py`, verificar que incluya:

1. **Docstring de cabecera**:
   ```python
   """
   Ejercicio XX: [Descripción clara del objetivo].
   """
   ```
2. **Importaciones al inicio** (si las hay): `import os`, `from pathlib import Path`.
3. **Separación lógica**: Funciones declaradas antes del código principal. Líneas en blanco entre bloques.

### Paso 3: Auditoría de Rutas y Secretos

- ✅ Recursos locales (imágenes, datasets) con rutas relativas dinámicas:
  ```python
  from pathlib import Path
  RUTA_RECURSO = Path(__file__).parent / "carpeta" / "archivo"
  ```
- ❌ **Prohibido**: rutas hardcodeadas dependientes del cwd (`open("imagenes/foto.jpg")`).
- ❌ **Prohibido**: credenciales, tokens o API keys hardcodeadas. Deben leerse con `os.environ.get()`.

### Paso 4: Auditoría de README.md por Carpeta

Verificar que cada carpeta contenga un `README.md` con las secciones obligatorias:
- `# Ejercicio/Material/Extra XX: [Título]`
- `## 📌 Enunciado` (o `## 📌 Descripción`)
- `## 🧠 Conceptos Aplicados`
- `## 📥 Ejemplo de Entrada / Salida` (si aplica)
- `## 🚀 Cómo ejecutar`

Verificar además que la carpeta figure en la tabla del catálogo del `README.md` raíz.

### Paso 5: Validación de Sintaxis Global

```bash
python -m compileall ejercicios/ buenas-practicas/ codigo-repetido/ extras/
```

### Paso 6: Generar Reporte de Auditoría

Producir un resumen con:

| Categoría | Estado | Detalles |
| :--- | :---: | :--- |
| Nomenclatura snake_case | ✅ / ⚠️ | Archivos con violaciones detectadas |
| Nombres declarativos | ✅ / ⚠️ | Variables crípticas o abreviadas |
| Docstrings de cabecera | ✅ / ⚠️ | Archivos sin docstring inicial |
| Rutas con pathlib | ✅ / ⚠️ | Scripts con rutas hardcodeadas |
| Secretos fuera del código | ✅ / ⚠️ | Credenciales hardcodeadas |
| README.md completos | ✅ / ⚠️ | Carpetas con secciones faltantes |
| Compilación exitosa | ✅ / ❌ | Errores de sintaxis |

---

## ⚠️ Consideraciones

- **No modificar la lógica funcional del código** durante la auditoría, solo la forma y los nombres.
- Si se encuentran violaciones, listarlas con la ubicación exacta (archivo y línea) y proponer la corrección.
- Al corregir, asegurar que el comportamiento y las salidas del programa se mantengan idénticos.
