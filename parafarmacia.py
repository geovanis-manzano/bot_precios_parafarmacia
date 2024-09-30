import requests
import json
import pandas as pd
import logging

class Parafarmacia:
    def __init__(self, config, token):
        # URL del servicio web Parafarmacia
        self.url_parafarmacia = config['api_urls']['parafarmacia_url']
        
        # Encabezados de la solicitud
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json'
        }
        
        # Parámetros de la solicitud
        self.params = config['parametros_parafarmacia']
        
        # Ruta para guardar el archivo Excel
        self.output_path = config['output_path_parafarmacia']

    def descargar_parafarmacia(self):
        logger = logging.getLogger()
        
        # Realizar la solicitud GET
        # print("Descargando parafarmacia ...")
        logger.info("Descargando parafarmacia ...")
        respuesta_parafarmacia = requests.get(self.url_parafarmacia, headers=self.headers, params=self.params)
        
        # Verificar el código de estado de la respuesta
        if respuesta_parafarmacia.status_code == 200:
            # La solicitud fue exitosa
            # print("Descarga de parafarmacia completada con exito")
            logger.info("Descarga de parafarmacia completada con exito")
        
            # Extraer el cuerpo de la respuesta HTTP
            cuerpo_respuesta_parafarmacia = respuesta_parafarmacia.text
        
            # Convertir el cuerpo de la respuesta JSON a un diccionario de Python
            respuesta_parafarmacia_diccionario = json.loads(cuerpo_respuesta_parafarmacia)

            # Acceder a la sección "Resultados"
            resultados = respuesta_parafarmacia_diccionario["Resultados"]

            # Crear un DataFrame de pandas con los datos
            df = pd.DataFrame(resultados)
            
            # Eliminar el símbolo '+' al inicio del campo "NombreCompleto", ya sea con o sin espacio
            df['NombreCompleto'] = df['NombreCompleto'].str.lstrip('+ ').str.lstrip('+')  

            # Guardar el DataFrame en un archivo Excel
            df.to_excel(self.output_path, index=False)

            # print(f"Datos almacenados en {self.output_path}")   
            logger.info(f"Datos almacenados en {self.output_path}")     
        
        else:
            # Hubo un error en la solicitud
            # print(f"Error en la solicitud del servicio web Parafarmacia: {respuesta_parafarmacia.status_code}")
            logger.error(f"Error en la solicitud del servicio web Parafarmacia: {respuesta_parafarmacia.status_code}")
        
            # Mostrar el cuerpo de la respuesta en caso de error
            # print(respuesta_parafarmacia.text)
            logger.error(respuesta_parafarmacia.text)
