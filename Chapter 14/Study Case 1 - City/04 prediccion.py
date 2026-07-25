# Realizar predicciones para nuevos datos (por ejemplo, para la próxima semana)
nuevos_datos = [[22, 55, 10, 1, 15, 0]]  # Datos de temperatura, humedad, etc.
nuevos_datos_scaled = scaler.transform(nuevos_datos)
prediccion = model.predict(nuevos_datos_scaled)
print(f'Predicción de demanda energética: {prediccion[0]} kWh')