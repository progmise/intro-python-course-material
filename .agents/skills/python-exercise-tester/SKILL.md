---
name: python-exercise-tester
description: >-
  Workflow para generar y ejecutar pruebas automatizadas sobre los ejercicios del repositorio.
  Diseña casos de prueba estándar y de borde usando unittest.mock para simular input(),
  ejecuta los tests y reporta resultados.
---

# Skill: Python Exercise Tester

Esta skill define el procedimiento para agregar pruebas automatizadas a cualquier material ejecutable
del repositorio **intro-python-course-material**, verificando que las soluciones produzcan las
salidas esperadas para distintos escenarios de entrada, incluyendo casos borde.

---

## 📋 Flujo de Trabajo

### Paso 1: Identificar el Material a Testear
1. Localizar la carpeta bajo `ejercicios/XX-nombre/` (o `extras/XX-nombre/` si es ejecutable).
2. Leer el `README.md` para entender la consigna, los ejemplos de I/O y los conceptos aplicados.
3. Leer el `main.py` para comprender la lógica implementada y detectar las funciones a testear.
4. **No testear** material de `codigo-repetido/` (código "antes" conservado a propósito)
   ni `extras/01-consumo-api` (requiere credencial real y acceso a red).

### Paso 2: Diseñar los Casos de Prueba
Diseñar al menos 3 categorías de test:

1. **Casos estándar (happy path)**: Entradas esperadas que producen el resultado correcto.
2. **Casos borde**: Valores límite, divisiones por cero, listas vacías, cadenas vacías, etc.
3. **Casos de validación**: Entradas inválidas que deben ser rechazadas o manejadas con un mensaje de error.

### Paso 3: Crear el Archivo de Tests
Crear el archivo `test_main.py` dentro de la misma carpeta del ejercicio, usando `unittest`:

```python
"""
Tests para Ejercicio XX: [Título del Ejercicio].
"""
import unittest
from unittest.mock import patch
from io import StringIO


class TestEjercicioXX(unittest.TestCase):

    @patch("builtins.input", side_effect=["valor1", "valor2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_caso_estandar(self, salida_capturada, mock_input):
        """Verifica el comportamiento con entradas válidas esperadas."""
        import importlib
        modulo = importlib.import_module("main")
        importlib.reload(modulo)

        resultado = salida_capturada.getvalue().strip()
        self.assertIn("texto_esperado", resultado)

    @patch("builtins.input", side_effect=["valor_borde"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_caso_borde(self, salida_capturada, mock_input):
        """Verifica el comportamiento con valores límite o extremos."""
        import importlib
        modulo = importlib.import_module("main")
        importlib.reload(modulo)

        resultado = salida_capturada.getvalue().strip()
        self.assertIn("texto_esperado", resultado)


if __name__ == "__main__":
    unittest.main()
```

> **IMPORTANTE**: Para ejercicios que definen funciones puras (sin `input()`), es preferible testear
> directamente la función importándola, sin necesidad de mockear `input()`.

### Paso 4: Funciones Puras — Testeo Directo
Si el ejercicio expone funciones reutilizables, testearlas directamente:

```python
import sys
sys.path.insert(0, ".")
from main import calcular_maximo

class TestCalculoExtremos(unittest.TestCase):
    def test_maximo_clasico(self):
        self.assertEqual(calcular_maximo([1, 4, 2, 99]), 99)

    def test_maximo_un_elemento(self):
        self.assertEqual(calcular_maximo([7]), 7)
```

### Paso 5: Ejecutar los Tests
```bash
# Ejecutar tests de un ejercicio específico
python -m pytest ejercicios/XX-nombre/test_main.py -v

# O con unittest directamente
cd ejercicios/XX-nombre/
python -m unittest test_main -v
```

### Paso 6: Reportar Resultados
- Si todos los tests pasan: Confirmar que el ejercicio está correctamente implementado.
- Si algún test falla: Identificar la causa, corregir el código y volver a ejecutar.
- Incluir en el reporte: Cantidad de tests ejecutados, pasados y fallidos.

---

## ⚠️ Consideraciones Importantes

- **No modificar la lógica original del ejercicio** para hacer que los tests pasen. Los tests deben reflejar
  las expectativas reales del enunciado.
- **Los archivos `test_main.py` no se incluyen en el `README.md` del catálogo central**, pero sí se mencionan
  en el `README.md` local si existen.
- Los ejercicios que leen recursos locales deben testearse asegurando que `Path(__file__).parent` resuelva
  correctamente cuando el test se ejecuta desde cualquier directorio.
