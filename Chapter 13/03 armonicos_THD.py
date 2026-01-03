# Cálculo de THD
fundamental = magnitudes_positivas[np.argmax(frecuencias_positivas == frecuencia_fundamental)]
armonicos = np.sqrt(np.sum(magnitudes_positivas**2) - fundamental**2)
thd = (armonicos / fundamental) * 100

print(f"Distorsión Armónica Total (THD): {thd:.2f}%")
