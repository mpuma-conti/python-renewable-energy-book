from scipy.stats import zscore

df['z_score'] = zscore(df['demanda_energia'])
df_sin_outliers = df[df['z_score'].abs() <= 3]
