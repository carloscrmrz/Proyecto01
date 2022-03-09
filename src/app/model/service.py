import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv('API_KEY')
API_DOMAIN=os.getenv('API_DOMAIN')

if __name__ == '__main__':
    print("This is not an usable Python script.\nUsage: python3 weather_app.py\n")
    os._exit(os.EX_OK)

def get_weather(lat, lon):
    payload = {'lat': lat, 'lon': lon, 'appid': API_KEY}
    r = requests.get(API_DOMAIN, params=payload)
    print(r.json());
