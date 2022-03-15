import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv('API_KEY')
API_DOMAIN=os.getenv('API_DOMAIN')

if __name__ == '__main__':
    print("This is not an usable Python script.\nUsage: python3 weather_app.py\n")
    os._exit(os.EX_OK)

# Funcion para obtener la informacion en JSON, a traves de la API proporcionada por
# OpenWeather, esta recibe latitud y longitud, asi como de manera opcional el tipo
# de unidad que queremos para mostrar nuestra temperatura.

def make_get_request(lat, lon, units='metric', lang='sp'):
    payload = {'lat': lat, 'lon': lon, 'units': units, 'appid': API_KEY, 'lang': lang}
    r = requests.get(API_DOMAIN, params=payload)
    return r

def convert_request_to_json(request):
    return r.json()
