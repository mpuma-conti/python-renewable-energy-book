from opcua import Client

# Conexión al servidor OPC-UA
client = Client("opc.tcp://192.168.1.20:4840")
client.connect()

# Acceder a una variable específica
node = client.get_node("ns=2;i=2")
value = node.get_value()
print(f"Valor de la variable: {value}")

# Escribir un nuevo valor en la variable
node.set_value(42)

client.disconnect()