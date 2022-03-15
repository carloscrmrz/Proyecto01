import json
from datetime import datetime, timedelta

if __name__ == '__main__':
    print("Usage: python3 weather_app.py\n")
    os._exit(os.EX_OK)

"""
 Funcion para escribir al archivo de cache al disco, esta recibe un
 diccionario de Python y lo convierte a un objeto tipo string, el 
 cual se escribe al disco, con el nombre de archivo dado.
 cache_dict: el diccionario el cual convertira se escribira a disco.
"""

def write_to_cache(cache_dict):
    path_to_cache = "weather_data_cache.txt"
    
    # Usaremos la funcion open para abrir nuestro archivo de cache, si este no
    # existiese la funcion open lo creara.
    # La funcion json.dumps convierte un objeto de Python en un cadena tipo 
    # JSON, haciendola perfecta para nuestro cache.
    with open(path_to_cache, 'w') as f:
        f.write(json.dumps(cache_dict))
        f.close()

"""
 Funcion auxiliar para obtener el archivo de cache, la funcion busca 
 el nombre del archivo dado donde se ejecuta el programa y convierte
 el texto en un diccionario de Python.
 Si no existe el archivo, simplemente regresa un diccionario vacio
 Regresa un diccionario de python para su uso.
"""
def read_from_cache():
    path_to_cache = "weather_data_cache.txt"
    
    # Usamos la funcion open para abrir el archivo, lo extrae completo y luego 
    # convierte la JSON string en un diccionario de Python y lo devuelve para
    # su uso.
    try:
        with open(path_to_cache, 'r') as f:
            cache_dict = json.loads(f.read())
            f.close()
    except:
        cache_dict = {}

    return cache_dict

"""
 Funcion auxiliar que nos permite checar de manera rapida si nuestra
 consulta guardada en cache aun es valida (menor a una hora).
 La funcion regresa False si la consuta ya no es valida, True si lo 
 sigue siendo.
"""
def is_cache_expired(hour_of_consult):
    delta = abs((datetime.now() - datetime.strptime(hour_of_consult, "%Y-%m-%d %H:%M")))
    if delta < timedelta(hours=1):
        return False
    else:
        return True
