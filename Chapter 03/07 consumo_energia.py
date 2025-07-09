import matplotlib.pyplot as plt
import pandas as pd

# Datos de ejemplo de consumo energético
datos = pd.DataFrame({
    'Fecha': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Consumo_kWh': [100, 120, 150, 130, 160, 170, 180, 200, 220, 210]
})

# Graficar el consumo de energía en el tiempo
plt.plot(datos['Fecha'], datos['Consumo_kWh'], marker='o')
plt.xlabel('Fecha')
plt.ylabel('Consumo de Energía (kWh)')
plt.title('Consumo de Energía a lo Largo del Tiempo')
plt.xticks(rotation=45)
plt.show()