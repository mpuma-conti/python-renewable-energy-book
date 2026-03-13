# Imputación por la media de la columna
df['demanda_energia'] = df['demanda_energia'].fillna(df['demanda_energia'].mean())
