from pymodbus.client.sync import ModbusTcpClient

# Configurar cliente Modbus
client = ModbusTcpClient("192.168.1.10", port=502)
client.connect()

# Leer datos del medidor
lectura = client.read_holding_registers(100, 2, unit=1)
print(f"Voltaje leído: {lectura.registers[0] / 10} V")

# Enviar comando para ajustar un generador
client.write_register(200, 120, unit=1)  # Ajustar salida a 120 kW

client.close()