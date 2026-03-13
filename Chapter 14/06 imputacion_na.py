# Imputación de valores faltantes con el valor anterior
df['demanda_energia'] = df['demanda_energia'].fillna(method='ffill')
