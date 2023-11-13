import csv
import pywhatkit as kit # WhatsApp
import pandas as pd # Manejo BD
import time
import tkinter as tk # Mensaje emergente
from tkinter import messagebox

# Leer el archivo CSV
df = pd.read_csv('csv/prueba.csv')

# Texto que deseas agregar antes del enlace
texto_adicional = "Buenos días, se les invita a confirmar su asistencia a la fiesta de XV años de nuestra hija Elisabet, ya que se realizará el cierre de la lista de invitados. Si no pueden abrir el enlace, favor de copiarlo y pegarlo en el navegador de su preferencia. Por su atención, gracias.  "
# otro_texto = " Atentamente, Familia Ortiz Garcia."
#Re-envio
# texto_adicional = "Buenos días, se les hace él reenvió de la preinvitación de nuestra hija Elisabet."

# Archivo de registro
archivo_de_registro = open('registro.txt', 'w')

# Iterar a través de las filas del DataFrame
for index, row in df.iterrows():
    numero = str(row['Telefono'])
    enlace = row['Enlace']
    
    # Construir el mensaje
    # mensaje = f"{texto_adicional}{enlace}{otro_texto}"
    # mensaje2 = f"{enlace}"
    mensaje = f"{texto_adicional}{enlace}"
    mensaje2 = f"{enlace}"

    try:
        # Enviar el mensaje a través de WhatsApp
        kit.sendwhatmsg_instantly(f'+{numero}', mensaje, 15, True, 4)
        print(f"Mensaje enviado a {numero}")
        # kit.sendwhatmsg_instantly(f'+{numero}', mensaje2, 17, True, 4)
    except Exception as e:
        error_msg = f"No se pudo enviar el mensaje a {numero}: {str(e)}"
        print(error_msg)
        archivo_de_registro.write(error_msg + '\n')

    # Esperar un momento entre cada envío (ajusta esto según tus necesidades)
    time.sleep(5)

archivo_de_registro.close()
print("Proceso completado.")

# Mostrar mensaje emergente
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Terminado", "Se han enviado todos los mensajes")
root.destroy()
