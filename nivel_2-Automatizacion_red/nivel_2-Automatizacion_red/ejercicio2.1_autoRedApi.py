"""Hacer ping a un sitio web y guardar los resultados.
🔹 6. Ping a servidores remotos

    ✅ Hacer ping a un servidor remoto y guardar los resultados.

    ➕ Aprende: subprocess, os.system, with.

"""

import subprocess
import os

def hacer_ping(sitio_web):
    try:
        resultado = subprocess.run(['ping', '-c', '5', sitio_web], capture_output=True, text=True, check=True)
        print(resultado.stdout)
        with open("output.txt", "w") as archivo:
            archivo.write(f"SITIO: {sitio_web}\n\n" + resultado.stdout)
        return True
        
    except subprocess.CalledProcessError:
        return False

sitio_web = 'www.youtube.com'

if hacer_ping(sitio_web):
    print(f"El ping a {sitio_web} fue realizado correctamente...")
else:
    print(f"No hubo respuesta a {sitio_web}...")