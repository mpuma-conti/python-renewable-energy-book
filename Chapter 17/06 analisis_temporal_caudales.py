# Análisis temporal: evolución del caudal a lo largo del tiempo
datos_hidraulicos['fecha'] = pd.to_datetime(datos_hidraulicos['fecha'])
plt.figure(figsize=(12, 6))
plt.plot(datos_hidraulicos['fecha'], datos_hidraulicos['caudal'])
plt.title('Evolución Temporal de los Caudales')
plt.xlabel('Fecha')
plt.ylabel('Caudal (m³/s)')
plt.xticks(rotation=45)
plt.show()