import logging
from logging.handlers import TimedRotatingFileHandler
import os

def setup_logger():
    # Cargar el nombre base del archivo de configuración o usar un nombre por defecto
    log_directory = "logs"
    log_filename = "bot_precio_parafarmacia.log"

    # Crear el directorio de logs si no existe
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Crear un handler que rota diariamente
    log_file_handler = TimedRotatingFileHandler(
        os.path.join(log_directory, log_filename), 
        when="midnight", # Rotar a medianoche
        interval=1, # Cada 1 dia
        backupCount=30 # Número de días de logs a mantener
    ) 
    
    # Especificar el formato del nombre de archivo cuando se rota
    log_file_handler.suffix = "%Y-%m-%d.log"  # Formato deseado para los logs rotados

    # Crear un handler para la consola (StreamHandler)
    console_handler = logging.StreamHandler()

    # Formato del log
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)
    log_file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Obtener el logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Añadir ambos handlers: archivo y consola
    logger.addHandler(log_file_handler)
    logger.addHandler(console_handler)

    return logger