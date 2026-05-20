df['fecha'] = pd.to_datetime(df['fecha'])
df.set_index('fecha', inplace=True)
df_diario = df.resample('D').mean()  # Promedio diario de la demanda energética