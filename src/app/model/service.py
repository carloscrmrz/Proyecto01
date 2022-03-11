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

def get_json_info(lat, lon, units='metric', lang='sp'):

    payload = {'lat': lat, 'lon': lon, 'units': units, 'appid': API_KEY, 'lang': lang}

    # Usaremos la biblioteca de requests para hacer (valga la redundancia) los
    # requests al servidor de OpenWeather, el metodo get crea nuestra URL a partir
    # del dominio que le pasamos de la API mas los parametros que creamos a partir
    # del diccionario 'payload'.

    r = requests.get(API_DOMAIN, params=payload)
    # Checamos que la URL este correcta.
    assert( r.url == f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={units}&appid={API_KEY}&lang={lang}" )

    # Ahora probamos que la respuesta del servidor sea exitosa.
    assert( r.status_code == 200 )

    # Para este punto ya tenemos nuestra respuesta del servidor, la cual
    # convertiremos a JSON y devolveremos para su proceso en la aplicacion
    return r.json()
