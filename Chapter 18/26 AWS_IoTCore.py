import boto3
from botocore.exceptions import NoCredentialsError

# Configuración del cliente AWS IoT
client = boto3.client('iot-data', region_name='us-west-2')

# Publicar un mensaje en un tópico MQTT
def publicar_mensaje(tópico, mensaje):
    try:
        response = client.publish(
            topic=tópico,
            qos=1,
            payload=mensaje
        )
        print("Mensaje publicado exitosamente")
    except NoCredentialsError:
        print("Credenciales no disponibles")

# Publicar un mensaje
publicar_mensaje("planta/hidro/turbina1", "Nivel de agua: 500m³")