"""
 Funcion que genera el reporte, crea una plantilla HTML y genera de
 manera dinamica la tabla donde se mostraran de manera mas amigable
 los datos obtenidos de la API.
 @param cache el cache que genera nuestra aplicacion.
"""
def generate(cache):
    path_to_html = "report.html"
    html = """
    <html>
    <head>
    <title>Reporte Aeropuertos</title>
    <meta charset="utf-8">
    <body>
    <table>
    <tr>\n
    \t<th>Aeropuerto</th>\n
    \t<th>Temperatura</th>\n
    \t<th>Temp. Min.</th>\n
    \t<th>Temp. Max.</th>\n
    \t<th>Descripcion</th>\n
    </tr>\n
    """
    for report in cache:
        html += create_table_row(cache[report])

    html += "</table></body></html>"

    with open(path_to_html, 'w') as f:
        f.write(html)
        f.close()

"""
 Funcion auxiliar que genera de manera dinamica las etiquetas HTML
 de nuestra tabla y las rellena con los datos de que se le 
 proporcionan a partir de los diccionarios sanitizados de datos.
 @param airport_dict el diccionario de datos del aeropuerto.
 @return el conjunto de etiquetas HTML que generan una fila en 
         nuestra tabla.
"""
def create_table_row(airport_dict):
    table = "<tr>\n"
    table += f"\t<th>{airport_dict['name']}</th>\n"
    table += f"\t<th>{airport_dict['temp']}°C</th>\n"
    table += f"\t<th>{airport_dict['temp_min']}°C</th>\n"
    table += f"\t<th>{airport_dict['temp_max']}°C</th>\n"
    table += f"\t<th>{airport_dict['weather']}</th>\n"
    table += "</tr>\n"

    return table
