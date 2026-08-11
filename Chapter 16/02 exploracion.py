import seaborn as sns
import matplotlib.pyplot as plt

# Visualización de la relación entre emisiones de CO2 y consumo de agua
sns.scatterplot(x='Emisiones_CO2', y='Consumo_Agua', data=df_clean)
plt.title('Relación entre Emisiones de CO2 y Consumo de Agua')
plt.show()