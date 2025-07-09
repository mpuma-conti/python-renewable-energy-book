# Simulación de nueva entrada de datos en tiempo real
nueva_entrada = [[30, 70, 2, 14]]  # Ejemplo de temperatura, humedad, día y hora

# Realizar la predicción en tiempo real
prediccion_tiempo_real = modelo_rf.predict(nueva_entrada)
print(f"Predicción en tiempo real del consumo: {prediccion_tiempo_real[0]} kWh")