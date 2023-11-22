import csv
import pywhatkit as kit
import pandas as pd
import time

# Leer el archivo CSV
df = pd.read_csv('csv/prueba.csv')

# Texto que deseas agregar antes del enlace
texto_adicional = "¡Echa un vistazo a este enlace: "

# Archivo de registro
archivo_de_registro = open('registro.txt', 'w')

# Iterar a través de las filas del DataFrame
for index, row in df.iterrows():
    numero = str(row['Telefono'])
    enlace = row['Enlace']
    
    # Construir el mensaje
    mensaje = f"{texto_adicional}{enlace}"

    try:
        # Enviar el mensaje a través de WhatsApp
        kit.sendwhatmsg_instantly(f'+{numero}', mensaje, 15, True, 4)
        print(f"Mensaje enviado a {numero}")
    except Exception as e:
        error_msg = f"No se pudo enviar el mensaje a {numero}: {str(e)}"
        print(error_msg)
        archivo_de_registro.write(error_msg + '\n')

    # Esperar un momento entre cada envío (ajusta esto según tus necesidades)
    time.sleep(5)

archivo_de_registro.close()
print("Proceso completado.")

