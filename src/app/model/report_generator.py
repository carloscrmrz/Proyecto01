def generate(cache):
    path_to_html = "report.html"
    html = """
    <html>
    <head>
    <title>Reporte Aeropuertos</title>
    <meta charset="utf-8">
    <body>
    <table>
    <tr>
    <th>Aeropuerto</th>
    <th>Temperatura</th>
    <th>Temp. Min.</th>
    <th>Temp. Max.</th>
    <th>Descripcion</th>
    </tr>
    """
    for report in cache:
        html += create_table_row(cache[report])

    html += "</table></body></html>"

    with open(path_to_html, 'w') as f:
        f.write(html)
        f.close()

def create_table_row(airport_dict):
    table = "<tr>"
    table += f"<th>{airport_dict['name']}</th>"
    table += f"<th>{airport_dict['temp']}°C</th>"
    table += f"<th>{airport_dict['temp_min']}°C</th>"
    table += f"<th>{airport_dict['temp_max']}°C</th>"
    table += f"<th>{airport_dict['weather']}</th>"
    table += "</tr>"

    return table
