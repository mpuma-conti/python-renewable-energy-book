from scipy.stats import linregress

# Análisis de regresión lineal entre emisiones de CO2 y generación de energía renovable
slope, intercept, r_value, p_value, std_err = linregress(df_clean['Generacion_Energia'], df_clean['Emisiones_CO2'])

print(f"Pendiente: {slope}, Intercepto: {intercept}")