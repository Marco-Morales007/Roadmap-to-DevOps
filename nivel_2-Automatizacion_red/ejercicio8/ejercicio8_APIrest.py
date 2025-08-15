"""
🔹 8. Llamada a una API REST (pública)

    ✅ Conéctate a una API (ej: JSONPlaceholder o OpenWeather) y muestra datos útiles.

    ➕ Aprende: requests, json, manejo de errores.
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables desde .env

API_KEY = os.getenv('OPENWEATHER_API_KEY')

#POR CIUDAD
ciudad = input("Ciudad: ")
url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es'

#POR LATITUD Y LONGITUD
#lat = float(input("Latitud: "))
#lon = float(input("Longitud: "))
#url2 = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=es'

respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()
    print(f"Ciudad: {datos['name']}")
    print(f"Temperatura: {datos['main']['temp']}°C")
    print(f"Clima: {datos['weather'][0]['description']}")
else:
    print(f"Error al obtener datos: {respuesta.status_code}")
