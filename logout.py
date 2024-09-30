import requests
import logging

class Logout:
    def __init__(self, config, token):
        # URL del servicio web Logout
        self.url_logout = config['api_urls']['logout_url']
        
        # Encabezados de la solicitud
        self.headers = {
            'Authorization': f'Bearer {token}'
        }

    def cerrar_sesion(self):
        logger = logging.getLogger()
        
        # Realizar la solicitud POST
        respuesta_logout = requests.get(self.url_logout, headers=self.headers)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if respuesta_logout.status_code == 200:
            # print('La sesión de BotPlus ha sido cerrada exitosamente')
            logger.info('La sesión de BotPlus ha sido cerrada exitosamente')
        else:
            # print(f'Error al cerrar la sesión de BotPlus: {respuesta_logout.status_code}')
            logger.error(f'Error al cerrar la sesión de BotPlus: {respuesta_logout.status_code}')
        
            # Mostrar el cuerpo de la respuesta en caso de error
            # print(respuesta_logout.text)
            logger.error(respuesta_logout.text)
