# Ejercicio 09: Menú de Países

## 📌 Enunciado
Crear un programa con un menú que permita:

1. **Cargar datos de países**: nombre, cantidad de registros y dólares invertidos (la carga termina al ingresar un nombre vacío; no se admiten países duplicados).
2. **Mostrar** la información de los países con más de 50.000 USD invertidos.
3. **Mostrar el índice** de USD invertidos totales / registros totales.
4. **Salir** ingresando `*`.

Cada país se almacena como una lista `[nombre, registros, dolares]` dentro de una lista de países.

## 🧠 Conceptos Aplicados
- Listas de listas para registros heterogéneos.
- Búsqueda lineal para detectar duplicados.
- Filtrado por umbral y acumuladores para estadísticas.
- Menú interactivo con centinela `*` y guarda de división por cero.

## 📥 Ejemplo de Entrada / Salida
- **Entrada**: opción `1` → `Argentina`, `100` registros, `75000` USD → enter; opción `2`
  - **Salida**: `- Argentina: 100 registros, 75,000.00 USD`

## 🚀 Cómo ejecutar
```bash
python main.py
```
