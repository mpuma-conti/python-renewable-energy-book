# Ejemplo de modularidad
def leer_sensor(sensor_id):
    # Implementación de lectura de sensor
    pass

def procesar_datos(dato):
    # Implementación de procesamiento de datos
    pass

def enviar_comando(actuador_id, comando):
    # Implementación de envío de comandos
    pass

def main():
    dato = leer_sensor('temperatura')
    dato_procesado = procesar_datos(dato)
    enviar_comando('valvula1', dato_procesado)

if __name__ == "__main__":
    main()