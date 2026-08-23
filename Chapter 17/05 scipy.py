from scipy import stats

# Estimación de la distribución de probabilidad para los caudales
caudal_promedio = np.mean(caudales)
caudal_std = np.std(caudales)

# Distribución normal
distribucion = stats.norm(caudal_promedio, caudal_std)

# Evaluar la probabilidad de que el caudal sea menor a un valor específico
probabilidad = distribucion.cdf(100)
print(f"Probabilidad de que el caudal sea menor a 100 m³/s: {probabilidad:.2f}")