import model.service as service
import model.cache_processor as cache
import model.dict_creator as dc
import model.report_generator as report
import csv
from time import sleep


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
                if line_count == 100:
                    break
                # Sabemos que las columnas 2,3 son las coordenadas de nuestro aeropuerto de origen
                # mientras que las columnas 4,5 son las coordenadas del aeropuerto destino.
                # Estas columnas las obtenemos con row[i].

                process_data(row)
                line_count += 1
    report.generate(airport_cache)
    cache.write_to_cache(airport_cache)

def is_in_cache(iata):
    if iata in airport_cache:
        return True
    return False

def process_airport(row, dest_origin_flag):
    iata = row[dest_origin_flag]
    if dest_origin_flag == 0:
        i = 2
    else: 
        i = 4

    if not is_in_cache(iata):
        airport_origin = service.get_json_info(row[i], row[i+1])
        airport_cache[iata] = dc.create_dict(airport_origin, iata)
    else:
        if cache.is_cache_expired(airport_cache[iata]["time_of_consult"]):
            airport_origin = service.get_json_info(row[i], row[i+1])
            airport_cache[iata] = dc.create_dict(airport_origin, iata)

def process_data(row):
    process_airport(row, 0)
    process_airport(row, 1)

if __name__ == '__main__':
    main()
