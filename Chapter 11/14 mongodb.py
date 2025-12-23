from pymongo import MongoClient

# Conexión a MongoDB
cliente = MongoClient('mongodb://localhost:27017/')
db = cliente['monitoreo_energia']
coleccion = db['mediciones']

# Inserción de datos
dato = {
    "corriente": 5.2,
    "voltaje": 220.5,
    "potencia": 1147.26,
    "timestamp": "2024-11-24T12:00:00"
}
coleccion.insert_one(dato)
print("Dato insertado:", dato)

# Consultar los datos
for documento in coleccion.find():
    print(documento)

# Filtrar datos por rango de potencia
for documento in coleccion.find({"potencia": {"$gt": 1000}}):
    print("Dato con potencia > 1000:", documento)