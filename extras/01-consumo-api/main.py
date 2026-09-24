"""
Extra 01: Consumo de una API REST.

Ejemplo de consulta a API-Sports (football) con la librería requests.

⚠️ La API key NO debe estar hardcodeada en el código ni subirse a un
repositorio. Se lee de la variable de entorno API_SPORTS_KEY:

    # Windows (PowerShell)
    $env:API_SPORTS_KEY = "tu-clave"

    # Linux / macOS
    export API_SPORTS_KEY="tu-clave"

Requiere: pip install requests
"""

import os
import sys

import requests

URL: str = "https://v3.football.api-sports.io/leagues"

api_key: str | None = os.environ.get("API_SPORTS_KEY")

if not api_key:
    sys.exit("Error: definir la variable de entorno API_SPORTS_KEY con tu clave de API-Sports.")

headers: dict = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": api_key
}

response = requests.get(URL, headers=headers, timeout=30)
response.raise_for_status()

print(response.text)
