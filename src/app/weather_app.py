import model.service
import json
import csv
import time

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
                fp = model.service.get_json_info(row[2],row[3])
                print(f'Clima aeropuerto ({row[0]}) origen: {fp["main"]["temp"]}')
                fp = model.service.get_json_info(row[4],row[5])
                print(f'Clima aeropuerto ({row[1]}) destino: {fp["main"]["temp"]}')
                line_count += 1
                time.sleep(5)

if __name__ == '__main__':
    main()
