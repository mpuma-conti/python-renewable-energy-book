import pandas as pd

# Datos de ejemplo de consumo de energía en kWh
datos = pd.DataFrame({
    'Consumo_kWh': [100, 150, 200, 250, 300, 350]
})

# Obtener el resumen estadístico
resumen = datos.describe()
print(resumen)