from Crypto.Cipher import AES
import base64

# Clave secreta (debe ser de 16, 24 o 32 bytes)
key = b'mysecretpassword'
cipher = AES.new(key, AES.MODE_EAX)

# Encriptar mensaje
data = "Datos críticos de red"
ciphertext, tag = cipher.encrypt_and_digest(data.encode())

print(f"Datos encriptados: {base64.b64encode(ciphertext).decode()}")

# Desencriptar mensaje
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
plaintext = cipher_dec.decrypt(ciphertext).decode()
print(f"Datos desencriptados: {plaintext}")