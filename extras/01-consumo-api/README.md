# Extra 01: Consumo de una API REST

## 📌 Descripción
Ejemplo de consulta HTTP `GET` a la API de [API-Sports](https://www.api-football.com/) (endpoint `/leagues`) con la librería `requests`.

⚠️ **La API key no está en el código**: se lee de la variable de entorno `API_SPORTS_KEY`. Nunca subir credenciales a un repositorio.

## 🧠 Conceptos Aplicados
- Requests HTTP con headers de autenticación (`x-rapidapi-key`).
- Variables de entorno con `os.environ.get()` para manejar secretos.
- `requests.get()` con `timeout` y `raise_for_status()`.

## 📦 Requisitos
```bash
pip install requests
```

Configurar la clave antes de ejecutar:

```powershell
# Windows (PowerShell)
$env:API_SPORTS_KEY = "tu-clave"
```
```bash
# Linux / macOS
export API_SPORTS_KEY="tu-clave"
```

## 🚀 Cómo ejecutar
```bash
python main.py
```
