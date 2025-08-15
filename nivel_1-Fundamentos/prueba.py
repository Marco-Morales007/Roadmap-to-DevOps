"""
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Que rollo plebes, fierro")
ventana.geometry("800x600")  # Ancho x Alto

# Iniciar el bucle principal de la ventana
ventana.mainloop()
"""

dic = {
    'nombre' : "MARCO",
    'apellido' : 'MORALES',
    'edad' : 23,
}

dic['ciudad'] = ['Reynosa']
dic['ciudad'].append('Monterrey')

print(dic.items())