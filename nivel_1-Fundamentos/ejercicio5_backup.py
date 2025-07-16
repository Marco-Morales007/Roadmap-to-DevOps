#Ejercicio 5 hacer un backup local y guardar un log.

import os
import logging
import shutil


logging.basicConfig(
    filename= 'archivo_log.log',
    encoding='utf-8',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

logger = logging.getLogger(__name__)

path1 = '/home/tilin/Desktop/my_project/nivel_1-Fundamentos/archivos_txt_ejemplo/' #source
path2 = '/home/tilin/Desktop/my_project/nivel_1-Fundamentos/backup/' #dest

#crear el directorio (carpeta) si no existe
os.makedirs(os.path.dirname(path2), exist_ok=True)

files = os.listdir(path1)
#print(files)

for names in files:
    source = path1 + names
    dest = path2 + names
    try:
        shutil.copy(source, dest)
    except FileNotFoundError:
        logger.error(f"Archivo de origen {source} no encontrado....")
        print(f"Error: Archivo de origen {source} No existe")
    except PermissionError:
        logger.error(f"Error de permisos de la carpeta destino {dest}")
        print(f"No se tienen permisos para copiar al directorio {dest} .")
    except Exception as error:
        logger.error(f"Error inesperado....\n{error}")
        print(f"Ocurrio un error inesperado: {error}")

logger.info("Archivos copiados correctamente....")
#logger.info(files)

print(os.listdir(path2))



