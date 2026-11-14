import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Conectado con código de resultado " + str(rc))
    client.subscribe("parque-eolico/turbina/#")

def on_message(client, userdata, msg):
    datos = json.loads(msg.payload.decode())
    print(f"Turbina {datos['turbina_id']}: Viento {datos['velocidad_viento']} m/s, Dirección {datos['direccion_viento']}°")
    # Implementar lógica para detectar condiciones de fallo

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.parque-eolico.local", 1883, 60)
client.loop_forever()