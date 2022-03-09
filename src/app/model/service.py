import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv('API_KEY')
API_DOMAIN=os.getenv('API_DOMAIN')

if __name__ == '__main__':
    print("This is not an usable Python script.\nUsage: python3 weather_app.py\n")
    os._exit(os.EX_OK)

def get_json_info(lat, lon, units='metric'):
    payload = {'lat': lat, 'lon': lon, 'units': units, 'appid': API_KEY}
    r = requests.get(API_DOMAIN, params=payload)
    ## Checamos que la URL este correcta.
    assert( r.url == f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={units}&appid={API_KEY}" )

    ## Ahora probamos que la respuesta del servidor sea exitosa.
    assert( r.status_code == 200 )

    ## Para este punto ya tenemos nuestro JSON con la temperatura requerida en Kelvin
    return r.json()
