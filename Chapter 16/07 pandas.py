import pandas as pd
import matplotlib.pyplot as plt

# Simulamos algunos resultados del análisis LCA
data = {
    'Impacto': ['Emisiones de CO2', 'Consumo de agua', 'Uso de materiales', 'Efectos en biodiversidad'],
    'Valor': [200, 50, 120, 30]  # Valores hipotéticos para cada tipo de impacto
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Graficar los resultados
plt.bar(df['Impacto'], df['Valor'])
plt.xlabel('Tipo de Impacto Ambiental')
plt.ylabel('Valor del Impacto')
plt.title('Impacto Ambiental de un Sistema Fotovoltaico')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
