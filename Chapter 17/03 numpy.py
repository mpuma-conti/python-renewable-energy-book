import numpy as np

# Calcular la media de los caudales
caudales = datos_hidraulicos['caudal']
media_caudales = np.mean(caudales)
print(f"Caudal promedio: {media_caudales} m³/s")