import pandas as pd

# Crear un DataFrame con datos de variables de generación eólica
datos_eolica = pd.DataFrame({
    'Fecha': pd.date_range(start='2023-01-01', periods=10, freq='H'),
    'Velocidad_Viento': [10, 12, 9, 11, 13, 14, 15, 13, 12, 10],
    'Temperatura': [15, 16, 17, 15, 18, 19, 20, 21, 20, 19],
    'Generacion_kWh': [100, 120, 110, 115, 130, 140, 145, 135, 130, 120]
})
print(datos_eolica.head())