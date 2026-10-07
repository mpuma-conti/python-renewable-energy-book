import can

# Configuración del bus CAN
bus = can.interface.Bus(channel='can0', bustype='socketcan')

# Enviar un mensaje CAN
msg = can.Message(arbitration_id=0x123, data=[0x11, 0x22, 0x33], is_extended_id=False)
bus.send(msg)

# Recibir mensajes CAN
for msg in bus:
    print(f"ID: {msg.arbitration_id}, Data: {msg.data}")