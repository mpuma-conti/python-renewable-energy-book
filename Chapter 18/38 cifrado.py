from cryptography.fernet import Fernet

# Generación de una clave y creación de un objeto Fernet
clave = Fernet.generate_key()
cifrado = Fernet(clave)

# Encriptar un mensaje
mensaje = "Datos sensibles de la planta"
mensaje_encriptado = cifrado.encrypt(mensaje.encode())
print(f"Mensaje encriptado: {mensaje_encriptado}")

# Desencriptar el mensaje
mensaje_desencriptado = cifrado.decrypt(mensaje_encriptado)
print(f"Mensaje desencriptado: {mensaje_desencriptado.decode()}")