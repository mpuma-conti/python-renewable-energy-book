from sklearn.preprocessing import MinMaxScaler

# Crear variables de día de la semana y hora del día
datos['Dia_semana'] = pd.to_datetime(datos['Fecha']).dt.dayofweek
datos['Hora_dia'] = pd.to_datetime(datos['Hora']).dt.hour

# Normalizar las variables de entrada
escalador = MinMaxScaler()
datos_normalizados = escalador.fit_transform(datos[['Consumo_kWh', 'Temperatura', 'Humedad']])
print(datos_normalizados[:5])