import sqlite3

# Conexión a la base de datos (se crea si no existe)
conexion = sqlite3.connect('energia.db')

# Creación de tabla para almacenar datos energéticos
with conexion:
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mediciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        corriente REAL,
        voltaje REAL,
        potencia REAL
    )
    """)
    print("Tabla creada exitosamente.")

import random

# Función para simular inserción de datos
def insertar_datos(corriente, voltaje, potencia):
    with conexion:
        cursor = conexion.cursor()
        cursor.execute("""
        INSERT INTO mediciones (corriente, voltaje, potencia)
        VALUES (?, ?, ?)""", (corriente, voltaje, potencia))
        print("Datos insertados:", corriente, voltaje, potencia)

# Simulación de datos
for _ in range(5):
    corriente = random.uniform(0, 10)
    voltaje = random.uniform(210, 230)
    potencia = corriente * voltaje
    insertar_datos(corriente, voltaje, potencia)

# Consultar datos almacenados
with conexion:
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM mediciones ORDER BY timestamp DESC")
    for fila in cursor.fetchall():
        print(fila)