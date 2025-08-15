"""
🔹 7. Monitor simple de espacio en disco

    ✅ Verifica cuánto espacio queda en disco, y si baja de un umbral, lanza una alerta.

    ➕ Aprende: psutil o os.statvfs.
    
"""

import psutil
import logging

logging.basicConfig(
    filename='info.log',
    encoding='utf-8',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

path = '/home/tilin/Desktop/my_project/nivel_2-Automatizacion_red'
uso = psutil.disk_usage(path)
print(f"\nEspacio total: {uso.total // (1024**3)} GB")
print(f"Espacio usado: {uso.used // (1024**3)} GB")
print(f"Espacio libre: {uso.free // (1024**3)} GB")
print(f"Porcentaje en uso: {uso.percent}%")

if psutil.disk_usage(path).percent > 50:
    alerta = "Queda menos de 50% de espacio libre..."
    print(alerta)
    logger.warning(alerta)
else:
    alerta = "Espacio suficiente..."
    print(alerta)
    logger.info(alerta)

logger.info(
    f"Espacio total: {uso.total // (1024**3)} GB\n"
    f"Espacio usado: {uso.used // (1024**3)} GB\n"
    f"Espacio libre: {uso.free // (1024**3)} GB\n"
    f"Porcentaje en uso: {uso.percent}%"
    )