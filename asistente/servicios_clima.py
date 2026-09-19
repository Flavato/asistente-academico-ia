import os

import requests
from dotenv import load_dotenv


load_dotenv()


def describir_clima(codigo):
    if codigo == 0:
        return "Cielo despejado"

    if codigo in [1, 2, 3]:
        return "Parcialmente nublado"

    if codigo in [45, 48]:
        return "Niebla"

    if codigo in [51, 53, 55, 56, 57]:
        return "Llovizna"

    if codigo in [61, 63, 65, 66, 67]:
        return "Lluvia"

    if codigo in [71, 73, 75, 77]:
        return "Nieve"

    if codigo in [80, 81, 82]:
        return "Chaparrones"

    if codigo in [95, 96, 99]:
        return "Tormenta"

    return "Estado meteorológico variable"


def consultar_clima():
    api_url = os.getenv("WEATHER_API_URL")
    latitud = os.getenv("WEATHER_LATITUDE")
    longitud = os.getenv("WEATHER_LONGITUDE")
    ciudad = os.getenv("WEATHER_CITY", "Mendoza")

    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": (
            "temperature_2m,"
            "apparent_temperature,"
            "weather_code"
        ),
        "timezone": "America/Argentina/Mendoza",
    }

    try:
        respuesta = requests.get(
            api_url,
            params=parametros,
            timeout=10,
        )

        respuesta.raise_for_status()
        datos = respuesta.json()
        actual = datos["current"]

        return {
            "ciudad": ciudad,
            "temperatura": actual["temperature_2m"],
            "sensacion": actual["apparent_temperature"],
            "estado": describir_clima(actual["weather_code"]),
        }

    except (requests.RequestException, KeyError, ValueError):
        return {
            "error": (
                "No fue posible consultar el clima en este momento."
            )
        }