from statsmodels.tsa.seasonal import seasonal_decompose

# Datos de ejemplo de serie temporal de consumo energético
datos.set_index('Fecha', inplace=True)
serie_consumo = datos['Consumo_kWh']

# Descomposición aditiva
descomposicion = seasonal_decompose(serie_consumo, model='additive', period=7)
descomposicion.plot()
plt.show()