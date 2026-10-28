import serial

try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    dato = ser.readline().decode('utf-8').rstrip()
    print(f"Dato recibido: {dato}")
except serial.SerialException as e:
    print(f"Error en la conexión serial: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    ser.close()