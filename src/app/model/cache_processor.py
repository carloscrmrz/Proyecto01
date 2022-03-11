import json

if __name__ == '__main__':
    print("Usage: python3 weather_app.py\n")
    os._exit(os.EX_OK)

def write_to_cache(cache_dict):
    path_to_cache = "weather_data_cache.txt"
    
    # Usaremos la funcion open para abrir nuestro archivo de cache, si este no
    # existiese la funcion open lo creara.
    # La funcion json.dumps convierte un objeto de Python en un cadena tipo 
    # JSON, haciendola perfecta para nuestro cache.
    with open(path_to_cache, 'w') as f:
        f.write(json.dumps(cache_dict))
        f.close()

def read_from_cache():
    path_to_cache = "weather_data_cache.txt"
    
    # Usamos la funcion open para abrir el archivo, lo extrae completo y luego 
    # convierte la JSON string en un diccionario de Python y lo devuelve para
    # su uso.
    with open(path_to_cache, 'r') as f:
        cache_dict = json.loads(f.read())
        f.close()
        
    return cache_dict
