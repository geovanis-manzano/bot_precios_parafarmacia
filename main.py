import json
from autenticacion import Autenticacion
from precios import PreciosMedicamentos
from parafarmacia import Parafarmacia
from logout import Logout
from concurrent.futures import ThreadPoolExecutor
from logger import setup_logger

# Configurar el logger al inicio de la aplicación
setup_logger()

# Cargar configuración
with open('config.json', 'r') as f:
    config = json.load(f)

# Autenticación
autenticacion = Autenticacion(config)
token = autenticacion.obtener_token()

# Crear instancias para las descargas
precios_medicamentos = PreciosMedicamentos(config, token)
parafarmacia = Parafarmacia(config, token)

# Definir funciones que se ejecutarán en paralelo
def descargar_precios():
    precios_medicamentos.descargar_precios()

def descargar_parafarmacia():
    parafarmacia.descargar_parafarmacia()

# Ejecutar las descargas en paralelo
with ThreadPoolExecutor() as executor:
    futures = []
    futures.append(executor.submit(descargar_precios))
    futures.append(executor.submit(descargar_parafarmacia))

    # Esperar que ambas tareas terminen
    for future in futures:
        future.result()  # Si ocurre una excepción, será lanzada aquí

# Cerrar sesión
logout = Logout(config, token)
logout.cerrar_sesion()
