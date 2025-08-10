import os

dic = {}

for (root, dirs, files) in os.walk('/home/tilin/Desktop/my_project/nivel_1-Fundamentos'):
    for name in files:
        if name not in dic:
            dic[name] = []
        dic[name].append(root)

for (archivos, rutas) in dic.items():
    if len(rutas)>1:
        print(f"Archivo: {archivos}")
        for nombre in rutas:
            print(nombre + "/" + archivos)
        