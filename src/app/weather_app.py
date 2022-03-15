import model.service as service
import model.cache_processor as cache
import model.dict_creator as dc
import model.report_generator as report
import csv
from time import sleep

try: 
    airport_cache = cache.read_from_cache()
except:
    airport_cache = {}


def main():
    with open('dataset1.csv') as airport_data_file:
        airport_data = csv.reader(airport_data_file, delimiter=',')
        line_count = 0
        for row in airport_data:
            if line_count == 0:
                line_count += 1
            else:
                if line_count % 1000 == 0: # Se hizo esto porque la API se enoja si recibe muchas peticiones muy rapido.
                    sleep(60)
                process_data(row)

    report.generate(airport_cache)
    cache.write_to_cache(airport_cache)

"""
 Funcion auxiliar para saber si el diccionario buscado ya existe
 en nuestro cache.
 @param iata el codigo IATA que es la llave de nuestro diccionario
 @return True si existe algun diccionario cuya llave sea el codigo
         que se introdujo, False de otra manera.
"""
def is_in_cache(iata):
    if iata in airport_cache:
        return True
    return False

"""
 Funcion auxiliar para procesar las peticiones de los aeropuertos.
 Esta se sirve de una bandera para indicar si el aeropuerto que
 introducimos es el de origen o de destino.
 @param row la fila de nuestro archivo CSV a procesar.
 @param dest_origin_flag la bandera para que nuestra funcion sepa
        si se trata de un aeropuerto de origen (0) o un aeropuerto
        de destino (1)
"""
def process_airport(row, dest_origin_flag):
    iata = row[dest_origin_flag]
    if dest_origin_flag == 0:
        i = 2
    else: 
        i = 4

    if not is_in_cache(iata):
        airport = service.convert_request_to_json(service.make_get_request(row[i], row[i+1]))
        airport_cache[iata] = dc.create_dict(airport, iata)
    else:
        if cache.is_cache_expired(airport_cache[iata]["time_of_consult"]):
            airport = service.convert_request_to_json(service.make_get_request(row[i], row[i+1]))
            airport_cache[iata] = dc.create_dict(airport, iata)

"""
 Funcion auxiliar para procesar una fila completa de nuestro CSV.
 @param row la fila de nuestro archivo CSV.
"""
def process_data(row):
    process_airport(row, 0)
    process_airport(row, 1)

if __name__ == '__main__':
    main()
