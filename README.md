**Integrantes**:
- Carlos Cabrera Ramirez
- Sergio Medina Guzman 


**Proyecto 01** para la clase de **Modelado y Programacion** con el profesor Jose Galaviz, Ximena Lezama y Karla Esquivel en la Facultad de Ciencias, UNAM. 

**Weather Consult** es una aplicacion que permite a partir de un CSV preformateado obtener un informe de la temperatura actual, asi como datos general del clima en un aeropuerto usando la API de [OpenWeather](https://openweathermap.org/) escrita en Python. 
# 🌡️ Uso Weather Consult

1. **Sistema Operativo:** Linux · Mac OS / OS X · Windows
2. **Version de Python:** Python 3.6+

### Prerrequisitos
Antes de instalar los modulos asegurate de que `pip3` este actualizado.
```
$ pip3 install pytest
$ pip3 install python-dotenv # To use enviroment variables defined in .env
$ pip3 install requests
```

Para hacer ejecutar las pruebas unitarias, nos situaremos en el directorio `src/app` y ejecutaremos el comando:
```
$ pytest
```

Para usarse requerimos situarnos en el directorio `src/app` y editar nuestro archivo `.env` anadiendo la llave de la [API de OpenWeather](https://openweathermap.org/current), hecho esto y con los modulos instalados solo tenemos que usar el comando:

```
$ python3 weather_app.py
```

Este producira dos archivos:

- `./weather_data_cache.txt`: aqui se guardan los ultimos requests hechos, para futuro uso de la aplicacion.
- `./report.html`: aqui se guarda el reporte de texto hecho por la aplicacion, para su consulta.

El reporte es un archivo HTML que se podra abrir con cualquier navegador web (no requiere una conexion activa a internet) donde podremos encontrar una tabla que nos permite observar las consultas hechas en la ultima hora.
