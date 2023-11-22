# Envio masivo de mensajes a traves de whatsapp automatico

El archivo ``envio_con_aviso`` envia los mensajes a los numeros de telefono que se encuentran en el archivo .csv y al finalizar de enviar el mensaje muestra un mensaje emergente de que se concluyo con el proceso.

El archivo ``envio_sin_aviso`` envia los mensajes a los numero de telefono que se encuentran en el archivo .csv y al finalizar de enviar el mensaje musetra un mensaje en consola de que se conluyo con el proceso.

La estructura del archivo .csv tiene que ser en formato separado por comas:

```numero_de_telefono_a_10_digitos,enlace```

Ejemplo: 
> 5555555555,google.com

Se recomienda activar el entorno virtual mediante el comando
```bash
.env/Scripts/activate 
```