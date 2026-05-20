# nueva característica que represente la media de la demanda de energía en los últimos días
df['demanda_media_7d'] = df['demanda_energia'].rolling(window=7).mean()
# estacionalidad
df['mes'] = df['fecha'].dt.month
df['dia_semana'] = df['fecha'].dt.weekday