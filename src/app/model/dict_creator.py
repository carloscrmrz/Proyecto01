def create_dict(json_data, iata):
    assert( isinstance(json_data, dict) )
    airport_info = {}
    airport_info["name"] = iata
    airport_info["weather"] = json_data["weather"][0]["description"]
    airport_info["temp"] = json_data["main"]["temp"]
    airport_info["temp_min"] = json_data["main"]["temp_min"]
    airport_info["temp_max"] = json_data["main"]["temp_max"]
    airport_info["feels_like"] = json_data["main"]["feels_like"]

    return airport_info
