import sqlite3

# Conexión y creación de tablas
conexion = sqlite3.connect('monitoreo_fotovoltaico.db')
with conexion:
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS datos_ambientales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        temperatura REAL,
        humedad REAL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS datos_electricos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        voltaje REAL,
        corriente REAL,
        potencia REAL
    )
    """)

# Función para insertar datos
def insertar_datos_ambientales(temperatura, humedad):
    with conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO datos_ambientales (temperatura, humedad) VALUES (?, ?)",
                       (temperatura, humedad))

def insertar_datos_electricos(voltaje, corriente, potencia):
    with conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO datos_electricos (voltaje, corriente, potencia) VALUES (?, ?, ?)",
                       (voltaje, corriente, potencia))
