Q1 = df['demanda_energia'].quantile(0.25)
Q3 = df['demanda_energia'].quantile(0.75)
IQR = Q3 - Q1

# Definir los límites para detectar outliers
limites_inferior = Q1 - 1.5 * IQR
limites_superior = Q3 + 1.5 * IQR

# Filtrar los outliers
df_sin_outliers = df[(df['demanda_energia'] >= limites_inferior) & (df['demanda_energia'] <= limites_superior)]
