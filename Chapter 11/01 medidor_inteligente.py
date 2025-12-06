from pymodbus.client.sync import ModbusSerialClient

# Configuración del cliente Modbus
client = ModbusSerialClient(
    method='rtu',
    port='COM3',  # Puerto del medidor
    baudrate=9600,
    timeout=1
)

# Lectura de registros de datos
if client.connect():
    response = client.read_input_registers(address=0, count=2, unit=1)
    if response.isError():
        print("Error al leer datos")
    else:
        energia = response.registers[0] / 100.0  # Conversión de la lectura
        print(f"Energía medida: {energia} kWh")
    client.close()
else:
    print("No se pudo conectar al medidor")