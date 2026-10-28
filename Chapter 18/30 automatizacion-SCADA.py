import time
from opcua import Client

def recopilar_datos(cliente, nodo_id, intervalo):
    nodo = cliente.get_node(nodo_id)
    while True:
        valor = nodo.get_value()
        print(f"Valor actual: {valor}")
        # Implementar lógica adicional, como almacenar datos o generar alertas
        time.sleep(intervalo)

# Conexión al servidor OPC-UA
cliente = Client("opc.tcp://192.168.1.20:4840")
cliente.connect()

# Iniciar la recopilación de datos
try:
    recopilar_datos(cliente, "ns=2;i=2", 10)  # Recopilar cada 10 segundos
except KeyboardInterrupt:
    print("Interrupción manual.")
finally:
    cliente.disconnect()