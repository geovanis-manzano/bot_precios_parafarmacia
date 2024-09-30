import requests
import json
import logging

class Autenticacion:
    def __init__(self, config):
        # URL del servicio web Login
        self.url_autenticacion = config['api_urls']['autenticacion_url']
        
        # Datos que se envian en la solicitud POST
        self.credenciales = config['credenciales_autenticacion']

    def obtener_token(self):
        logger = logging.getLogger()
        
        # Realizar la solicitud POST
        # print("Realizando autenticacion ...")
        logger.info("Realizando autenticacion ...")
        respuesta_autenticacion = requests.post(self.url_autenticacion, data=self.credenciales)
        
        # Verificar el codigo de estado de la respuesta
        if respuesta_autenticacion.status_code == 200:
            # La solicitud fue exitosa
            # print("Autenticacion completada con exito")
            logger.info("Autenticacion completada con exito")
        
            # Extraer el cuerpo de la respuesta HTTP
            cuerpo_respuesta_autenticacion = respuesta_autenticacion.text
    
            # Convertir el cuerpo de la respuesta JSON a un diccionario de Python
            respuesta_autenticacion_diccionario = json.loads(cuerpo_respuesta_autenticacion)

            # Extraer el token de autenticación
            token = respuesta_autenticacion_diccionario['Token']
            # print(f"Token: {token}")
            logger.info(f"Token: {token}")
            
            return token
        else:
            # Hubo un error en la solicitud
            # print(f"Error en la solicitud del servicio web de autenticacion: {respuesta_autenticacion.status_code}")
            logger.error(f"Error en la solicitud del servicio web de autenticacion: {respuesta_autenticacion.status_code}")
    
            # Mostrar el cuerpo de la respuesta en caso de error
            # print(respuesta_autenticacion.text)
            logger.error(respuesta_autenticacion.text)
