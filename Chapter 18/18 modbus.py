from pymodbus.client.sync import ModbusTcpClient

# Configuración del cliente Modbus
client = ModbusTcpClient('192.168.1.10', port=502)
client.connect()

# Leer 10 registros de holding a partir de la dirección 100
result = client.read_holding_registers(100, 10, unit=1)
print(result.registers)

# Escribir un valor en el registro 100
client.write_register(100, 12345, unit=1)

client.close()