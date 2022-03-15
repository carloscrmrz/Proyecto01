import model.report_generator as report
from datetime import datetime

def test_create_table_row():
    """
    Simulated sanitazed airport data
    """
    sanitized_data = {'name': "MEX", 'time_of_consult': datetime.now().strftime("%Y-%m-%d %H:%M"), 'weather': 'soleado', 'temp': 23, 'temp_min': 16, 'temp_max': 31, 'feels_like': 24}
    
    table = "<tr>\n"
    table += "\t<th>MEX</th>\n"
    table += "\t<th>23°C</th>\n"
    table += "\t<th>16°C</th>\n"
    table += "\t<th>31°C</th>\n"
    table += "\t<th>soleado</th>\n"
    table += "</tr>\n"

    assert report.create_table_row(sanitized_data) == table
