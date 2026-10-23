from azure.iot.device import IoTHubDeviceClient, Message

# Cadena de conexión del dispositivo
CONNECTION_STRING = "HostName=mi-iothub.azure-devices.net;DeviceId=mi-dispositivo;SharedAccessKey=clave"

# Crear cliente del dispositivo
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

# Definir el mensaje a enviar
mensaje = Message("Nivel de agua: 500m³")

# Enviar el mensaje
client.send_message(mensaje)
print("Mensaje enviado")

# Cerrar la conexión
client.shutdown()