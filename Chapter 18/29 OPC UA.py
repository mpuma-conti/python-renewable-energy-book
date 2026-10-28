from opcua import Client

# Conexión al servidor OPC-UA
cliente = Client("opc.tcp://192.168.1.20:4840")
cliente.connect()

# Acceder a una variable específica
nodo = cliente.get_node("ns=2;i=2")
valor = nodo.get_value()
print(f"Valor de la variable: {valor}")

# Escribir un nuevo valor en la variable
nodo.set_value(42)

cliente.disconnect()