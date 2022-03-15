import os
import model.service as s
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv('API_KEY')

def test_request():
    lat = 19; lon = 99
    url = f"http://api.openweathermap.org/data/2.5/weather?lat=19&lon=99&units=metric&appid={API_KEY}&lang=sp"
    request = s.make_get_request(lat,lon)
    assert request.url == url
    assert request.status_code == 200
