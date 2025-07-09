import os
import datetime

fecha = datetime.datetime.now()
path = "/home/tilin/Desktop/my_project/nivel_1-Fundamentos/ejercicio3/"
contador = 1

old_name = "texto1.txt"
#new_name = fecha.date()
#print(new_name)

"""
for file_name in os.listdir(path):
    fuente = path + file_name

    destino = str(fecha.date()) + str(contador) + ".txt"
    os.rename(fuente, destino)
    new_name = str(fecha.date())
    contador += 1
print("Todos los archivos renombrados correctamente...")
"""

for file_name in os.listdir(path):
    try:
        fuente = os.path.join(path, file_name) 
        new_name = str(fecha.date()) + "("+ str(contador) + ")" + ".txt"
        destino = os.path.join(path, new_name)
        os.rename(fuente, destino)
        print(f"File {fuente} renamed to {new_name}")
    except FileExistsError:
        print(f"Error: File {new_name} already exist...")
    except OSError as e:
        print(f"An OS error ocurred: {e}")
    contador += 1


