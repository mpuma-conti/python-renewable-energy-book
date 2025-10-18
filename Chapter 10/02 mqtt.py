import paho.mqtt.client as mqtt

# Función para manejar mensajes entrantes
def on_message(client, userdata, message):
    print(f"Mensaje recibido: {str(message.payload.decode('utf-8'))}")

# Configurar cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883)

# Suscripción a un canal
client.subscribe("redinteligente/sensores/voltaje")
client.loop_start()

# Publicar un dato simulado
client.publish("redinteligente/sensores/voltaje", "Voltaje: 230.5 V")
client.loop_stop()