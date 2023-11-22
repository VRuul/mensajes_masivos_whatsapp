import csv
import pywhatkit as kit # WhatsApp
import pandas as pd # Manejo BD
import time
import tkinter as tk # Mensaje emergente
from tkinter import messagebox

# Leer el archivo CSV
df = pd.read_csv('csv/prueba.csv')

# Texto que deseas agregar antes del enlace
texto = "Buenos días, se les invita a confirmar su asistencia a la fiesta de XV años de nuestra hija Elisabet, ya que se realizará el cierre de la lista de invitados. Si no pueden abrir el enlace, favor de copiarlo y pegarlo en el navegador de su preferencia. Por su atención, gracias.  "
texto_adicional = " Atentamente, Familia Ortiz Garcia."

# Archivo de registro
archivo_de_registro = open('registro.txt', 'w')

# Iterar a través de las filas del DataFrame
for index, row in df.iterrows():
    numero = str(row['Telefono'])
    enlace = row['Enlace']
    
    # Construir el mensaje
    mensaje = f"{texto}{enlace}{texto_adicional}"

    try:
        # Enviar el mensaje a través de WhatsApp
        kit.sendwhatmsg_instantly(f'+{numero}', mensaje, 15, True, 4)
        print(f"Mensaje enviado a {numero}")
    except Exception as e:
        error_msg = f"No se pudo enviar el mensaje a {numero}: {str(e)}"
        print(error_msg)
        archivo_de_registro.write(error_msg + '\n')

    # Esperar un momento entre cada envío
    time.sleep(5)

archivo_de_registro.close()
print("Proceso completado.")

# Mostrar mensaje emergente
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Terminado", "Se han enviado todos los mensajes")
root.destroy()
