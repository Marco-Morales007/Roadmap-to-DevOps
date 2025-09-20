"""
10. Analizador de logs 
    - Lee un archivo de log y saca estadísticas: errores por tipo, líneas con “ERROR”, etc. 
    - Aprende: manejo de texto, re (regex), listas, diccionarios.
"""


import re
from collections import defaultdict

def analizar_log(ruta_log):
    #diccionario para contar tipos de mensajes
    stats = defaultdict(int)

    #guardamos en una lista las líneas de error
    errores = []

    #Regex para detectar el nivel del log (INFO, ERROR, WARNING, etc.)
    patron = re.compile(r"\b(INFO|ERROR|WARNING|DEBUG)\b")

    try:
        with open(ruta_log, "r", encoding="utf-8") as f:
            for linea in f:
                match = patron.search(linea)
                if match:
                    nivel = match.group(1)
                    stats[nivel] += 1

                    if nivel == "ERROR":
                        errores.append(linea.strip())

        # Mostrar resultados
        print("Log stats:")
        for nivel, cantidad in stats.items():
            print(f"  {nivel}: {cantidad}")

        print("\nERROR lines:")
        for error in errores[:5]:  # mostrar solo primeros 5
            print(f"  {error}")

    except FileNotFoundError:
        print(f"El archivo {ruta_log} no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

#poner la ruta del archivo.log para su posterior analisis...
analizar_log("/home/antonius/Desktop/my_projects/Roadmap-to-DevOps/nivel_2-Automatizacion_red/ejercicio10/test.log")
