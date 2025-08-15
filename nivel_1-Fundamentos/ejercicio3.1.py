import os

path = "/home/tilin/Desktop/my_project/nivel_1-Fundamentos/archivos_txt_ejemplo/"
contador = 1
#print(os.listdir(path))

print(os.listdir(path))
#renombrar archivos
for file_names in os.listdir(path):
    source = path + file_names
    destination = path + "NEW_file" +"("+ str(contador) +")"+ ".txt"
    os.rename(source, destination)
    contador += 1
print("Los archivos fueron renombrados....")
print(os.listdir(path))


