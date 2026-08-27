# Análisis de correlación entre caudal y producción de energía
correlacion = datos_hidraulicos[['caudal', 'energia']].corr()
sns.heatmap(correlacion, annot=True, cmap='coolwarm')
plt.title('Correlación entre Caudal y Producción de Energía')
plt.show()