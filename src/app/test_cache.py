import model.dict_creator as dc
import model.cache_processor as cache
from datetime import datetime, timedelta

def test_dict_creation():
    """
    We will simulate some fake data that could be received from
    the API endpoint, to create our dictionaries were we will 
    store the data that we will present to the end user and 
    that we will store in our cache.
    """
    name = "MEX"; time_of_consult = datetime.now().strftime("%Y-%m-%d %H:%M"); weather = "soleado"; temp = 23
    temp_min = 18; temp_max = 28; feels_like = 23.5
    
    sanitized_data = {'name': name, 'time_of_consult': time_of_consult, 'weather': weather, 'temp': temp, 'temp_min': temp_min, 'temp_max': temp_max, 'feels_like': feels_like}

    # This dictionary has extra trash data, that must be dumped by the fuction.
    json_data = {'name': name, 'time_of_consult': time_of_consult, 'random_list': [1,2,3], 'weather': [{'description': weather, 'silly': 'test', 'one': 1}], 'random_dict': {'one': 1, 'two': 2}, 'hello': 'iamtrash', 'whereami': 23412, 'location': 'in my house', 'main': {'temp': temp, 'temp_min': temp_min, 'temp_max': temp_max, 'feels_like': feels_like }}
    airport_info = dc.create_dict(json_data, "MEX")

    assert json_data != airport_info
    assert airport_info == sanitized_data
    
def test_is_cache_expired():
    hour1 = (datetime.now() + timedelta(minutes=57)).strftime("%Y-%m-%d %H:%M") # 57 minutes from now.
    hour2 = (datetime.now() + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M") # 1 hour later
    hour3 = (datetime.now() + timedelta(hours=1,minutes=1)).strftime("%Y-%m-%d %H:%M") # 1 hour and 1 minutes later
    hour4 = (datetime.now() - timedelta(hours=23)).strftime("%Y-%m-%d %H:%M") # 23 hours later.
    hour5 = (datetime.now() + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M") # 5 minutes later

    assert cache.is_cache_expired(hour1) == False
    assert cache.is_cache_expired(hour2) == False # Gives us false bc some weird functionality
    assert cache.is_cache_expired(hour3) == True
    assert cache.is_cache_expired(hour4) == True
    assert cache.is_cache_expired(hour5) == False
    
