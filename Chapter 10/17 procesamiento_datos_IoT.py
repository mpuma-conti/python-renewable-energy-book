import paho.mqtt.client as mqtt
import pandas as pd

# Función de callback para recibir datos
def on_message(client, userdata, msg):
    print(f"Datos recibidos: {msg.payload.decode()}")
    # Simulación de almacenamiento en un DataFrame
    global data
    data = data.append({"Tiempo": pd.Timestamp.now(), "Consumo": float(msg.payload.decode())}, ignore_index=True)

# Configurar cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883)
client.subscribe("red_urbana/consumo")

# DataFrame para almacenamiento
data = pd.DataFrame(columns=["Tiempo", "Consumo"])

# Escuchar mensajes
print("Monitoreando consumo...")
client.loop_start()