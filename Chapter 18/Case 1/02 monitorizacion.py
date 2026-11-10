import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Conectado con código de resultado " + str(rc))
    client.subscribe("planta/solar/panel/#")

def on_message(client, userdata, msg):
    datos = json.loads(msg.payload.decode())
    print(f"Panel {datos['panel_id']}: Eficiencia {datos['eficiencia']}%")
    # Aquí se puede agregar lógica para alertas o mantenimiento

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.planta-solar.local", 1883, 60)
client.loop_forever()