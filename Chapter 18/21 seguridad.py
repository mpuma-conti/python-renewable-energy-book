from cryptography.fernet import Fernet

# Generación de una clave
clave = Fernet.generate_key()
f = Fernet(clave)

# Encriptar un mensaje
mensaje = "Datos sensibles de la planta hidroeléctrica"
mensaje_encriptado = f.encrypt(mensaje.encode())
print(f"Mensaje encriptado: {mensaje_encriptado}")

# Desencriptar el mensaje
mensaje_desencriptado = f.decrypt(mensaje_encriptado)
print(f"Mensaje desencriptado: {mensaje_desencriptado.decode()}")