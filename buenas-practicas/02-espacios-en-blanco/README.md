# Buenas Prácticas 02: Espacios en Blanco dentro del Código

## 📌 Descripción
Ejercicio estilo *two-sum*: dada una lista de tuplas `(gusto, precio)` y un presupuesto `k`, encontrar dos gustos de helado cuyos precios sumen exactamente `k`.

El archivo muestra el mismo código en dos versiones:

- **Incorrecta** (comentada): indentación irregular de 2 espacios, sangrías inconsistentes.
- **Correcta**: 4 espacios por nivel, además iterando directamente sobre las tuplas en lugar de usar índices.

## 🧠 Conceptos Aplicados
- Indentación consistente de 4 espacios (PEP 8).
- Uso de un diccionario como tabla de "ya vistos" para resolver en una sola pasada: O(n).
- Desempaquetado de tuplas en el `for`.

## 📥 Ejemplo de Entrada / Salida
- No requiere entrada.
  - **Salida**: `{150: 'Chocolate', 'Durazno': 100}`

## 🚀 Cómo ejecutar
```bash
python main.py
```
