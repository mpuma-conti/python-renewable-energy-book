import paho.mqtt.client as mqtt

# Definición de callbacks
def on_connect(client, userdata, flags, rc):
    print("Conectado con código de resultado " + str(rc))
    client.subscribe("planta/hidro/turbina1")

def on_message(client, userdata, msg):
    print(f"Mensaje recibido en {msg.topic}: {msg.payload.decode()}")

# Configuración del cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conexión al broker MQTT
client.connect("broker.hivemq.com", 1883, 60)

# Publicar un mensaje
client.publish("planta/hidro/turbina1", "Inicio de operación")

# Mantener el loop
client.loop_forever()