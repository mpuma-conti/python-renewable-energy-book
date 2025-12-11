import paho.mqtt.client as mqtt

# Configuración del cliente MQTT
broker = "broker.hivemq.com"
client = mqtt.Client("Energía")

# Publicar datos al broker
client.connect(broker)
client.publish("energia/consumo", "Consumo: 12.5 kWh")
print("Datos enviados al servidor MQTT")
client.disconnect()