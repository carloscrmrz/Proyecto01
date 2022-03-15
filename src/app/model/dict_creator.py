from datetime import datetime

if __name__ == '__main__':
    print("Usage: python3 weather_app.py\n")
    os._exit(os.EX_OK)

"""
 Funcion que permite sanitizar los datos que la API nos entrega.
 @param json_data diccionario de python con los datos de la API.
 @param iata el codigo IATA del aeropuerto consultado.
 @returns un diccionario con los datos necesarios para nuestro 
          generador de reportes.
"""
def create_dict(json_data, iata):
    assert( isinstance(json_data, dict) )
    airport_info = {}
    airport_info["name"] = iata
    airport_info["time_of_consult"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    airport_info["weather"] = json_data["weather"][0]["description"]
    airport_info["temp"] = json_data["main"]["temp"]
    airport_info["temp_min"] = json_data["main"]["temp_min"]
    airport_info["temp_max"] = json_data["main"]["temp_max"]
    airport_info["feels_like"] = json_data["main"]["feels_like"]

    return airport_info
