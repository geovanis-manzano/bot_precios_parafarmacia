import requests
import json
import pandas as pd
import logging

class PreciosMedicamentos:
    def __init__(self, config, token):
        # URL del servicio web Medicamentos Precios
        self.url_precios = config['api_urls']['medicamentos_precios_url']
        
        # Encabezados de la solicitud
        self.headers = {
            'content-type': 'application/json; charset=utf-8',
            'Authorization': f'Bearer {token}'
        }
        
        # Datos a enviar en la solicitud (en formato JSON)
        self.data = {
            "tipoRegistros": "MUH",
            "ids": config['ids_precios'],
            "campos": config['campos_precios'],
            "campoOrden": "NOMMUH"
        }
        
        # Ruta para guardar el archivo Excel
        self.output_path = config['output_path_precios']

    def descargar_precios(self):
        logger = logging.getLogger()
        
        # Realizar la solicitud POST
        # print("Descargando precios de medicamentos ...")
        logger.info("Descargando precios de medicamentos ...")
        respuesta_medicamentos_precios = requests.post(self.url_precios, headers=self.headers, json=self.data)
        
        # Verificar el codigo de estado de la respuesta del servicio web Medicamentos Precios
        if respuesta_medicamentos_precios.status_code == 200:
            # La solicitud fue exitosa
            # print("Descarga de precios de medicamentos completada con exito")
            logger.info("Descarga de precios de medicamentos completada con exito")
        
            # Extraer el cuerpo de la respuesta HTTP
            cuerpo_respuesta_medicamentos_precios = respuesta_medicamentos_precios.text
        
            # Convertir el cuerpo de la respuesta JSON a un diccionario de Python
            respuesta_medicamentos_precios_diccionario = json.loads(cuerpo_respuesta_medicamentos_precios)

            # Acceder a la sección "datos"
            datos = respuesta_medicamentos_precios_diccionario["datos"]

            # Crear un DataFrame de pandas con los datos
            df = pd.DataFrame(datos)
        
            # Reemplazar comas por puntos en las columnas PVLMUH y PVPMUH
            df['PVLMUH'] = df['PVLMUH'].str.replace(',', '.')
            df['PVPMUH'] = df['PVPMUH'].str.replace(',', '.')            

            # Guardar el DataFrame en un archivo Excel
            df.to_excel(self.output_path, index=False)

            # print(f"Datos almacenados en {self.output_path}")
            logger.info(f"Datos almacenados en {self.output_path}")         
        else:
            # Hubo un error en la solicitud
            # print(f"Error en la solicitud del servicio web Medicamentos Precios: {respuesta_medicamentos_precios.status_code}")
            logger.error(f"Error en la solicitud del servicio web Medicamentos Precios: {respuesta_medicamentos_precios.status_code}")  
        
            # Mostrar el cuerpo de la respuesta en caso de error
            # print(respuesta_medicamentos_precios.text)
            logger.error(respuesta_medicamentos_precios.text)
