import model.service as service
import model.cache_processor as cache
import model.dict_creator as dc
import csv
import time

# Diccionario donde guardamos nuestras peticiones ya procesadas, y el cual usaremos
# para mostrar nuestros datos.
try: 
    airport_cache = cache.read_from_cache()
except:
    airport_cache = {}


def main():
    # Abrimos nuestro dataset en CSV
    with open('dataset1.csv') as airport_data_file:
        airport_data = csv.reader(airport_data_file, delimiter=',')
        line_count = 0
        for row in airport_data:
            if line_count == 0:
                line_count += 1
            else:
                if line_count == 5:
                    break
                # Sabemos que las columnas 2,3 son las coordenadas de nuestro aeropuerto de origen
                # mientras que las columnas 4,5 son las coordenadas del aeropuerto destino.
                # Estas columnas las obtenemos con row[i].
                airport_origin = service.get_json_info(row[2],row[3])
                airport_cache[row[0]] = dc.create_dict(airport_origin, row[0])
                airport_dest = service.get_json_info(row[4],row[5])
                airport_cache[row[1]] = dc.create_dict(airport_dest, row[1])

                print(airport_cache)

                line_count += 1
    cache.write_to_cache(airport_cache)

if __name__ == '__main__':
    main()
