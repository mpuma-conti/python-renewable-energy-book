import hashlib

# Función para generar hash de una contraseña
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Almacenar hash de contraseñas
usuarios = {
    "admin": hash_password("admin123"),
    "operador": hash_password("op456")
}

# Función de autenticación
def autenticar(usuario, contraseña):
    if usuario in usuarios and usuarios[usuario] == hash_password(contraseña):
        return True
    return False

# Ejemplo de uso
print(autenticar("admin", "admin123"))  # True
print(autenticar("admin", "w