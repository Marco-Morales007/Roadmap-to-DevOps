"""Hacer ping a varios sitios web y guardar los resultados.
🔹 6. Ping a servidores remotos

    ✅ Haz ping a varios sitios web y guarda los resultados.

    ➕ Aprende: subprocess, os.system, with.
     
"""

import subprocess
import os

def hacer_ping(sitio):
    try:
        resultado = subprocess.run(['ping', '-c', '5', sitio], capture_output=True, text=True, check=True)
        print(resultado.stdout)
        with open("output.txt", 'a') as file:
            file.write(f"\nSITIO = {sitio}\n\n" + resultado.stdout)
        return True
    except subprocess.SubprocessError:
        return False
   
sitios_web = ['www.youtube.com', 'www.facebook.com', 'www.google.com']

for sitio in sitios_web:
    if hacer_ping(sitio):
        print(f"El ping al sitio web {sitio} fue exitoso...")
    else:
        print(f"Error al hacer ping al sitio {sitio}")