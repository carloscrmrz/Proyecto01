import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv('API_KEY')
API_DOMAIN=os.getenv('API_DOMAIN')

if __name__ == '__main__':
    print("Usage: python3 weather_app.py\n")
    os._exit(os.EX_OK)

"""
 Funcion para hacer nuestro GET Request al servicio que proporciona la API de OpenWeather.
 @param lat la latitud de donde queremos obtener la temperatura.
 @param lon la longitud de donde queremos obtener la temperatura.
 @param units (opcional) las unidades que se mostraran (metric o imperial o standard).
 @param lang (opcional) el lenguaje en el que se nos proporcionara la informacion.
 @returns el objeto request.
"""
def make_get_request(lat, lon, units='metric', lang='sp'):
    payload = {'lat': lat, 'lon': lon, 'units': units, 'appid': API_KEY, 'lang': lang}
    r = requests.get(API_DOMAIN, params=payload)
    return r

"""
 Funcion para convertir nuestro objeto request en un diccionario tipo JSON.
 @param request el objeto request.
 @returns un diccionario 
"""
def convert_request_to_json(request):
    return request.json()
