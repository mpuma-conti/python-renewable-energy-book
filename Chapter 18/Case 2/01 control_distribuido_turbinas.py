import socket
import json
import time

def enviar_datos(turbina_id, velocidad_viento, direccion_viento):
    datos = {
        'turbina_id': turbina_id,
        'velocidad_viento': velocidad_viento,
        'direccion_viento': direccion_viento
    }
    mensaje = json.dumps(datos)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('192.168.1.20', 5000))
        s.sendall(mensaje.encode())
        respuesta = s.recv(1024)
        print(f"Respuesta del servidor: {respuesta.decode()}")

while True:
    # Simulación de lectura de sensores
    turbina = 1
    velocidad = 12.5  # m/s
    direccion = 180  # grados
    enviar_datos(turbina, velocidad, direccion)
    time.sleep(10)  # Enviar cada 10 segundos