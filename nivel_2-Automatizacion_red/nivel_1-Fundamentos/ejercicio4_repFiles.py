#programa para encontrar archivos repetidos
import os
dic = {}

for(root, dirs, files) in os.walk("/home/tilin/Desktop/my_project/nivel_1-Fundamentos"):
   for name in files:
      if name not in dic:
         dic[name] = []
      dic[name].append(root)
   
print(f"Archivos repetidos por nombre: ")
for (archivo, rutas) in dic.items():
   if len(rutas)>1:
      print(f"Archivo: {archivo}: ")
      for ruta in rutas:
         print(f"- {ruta}" + "/" + archivo)

#print(dic)
    

"""
for root, dirs, files in os.walk("/home/tilin/Desktop/my_project", topdown=True):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
"""

