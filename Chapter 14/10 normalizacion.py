#Normalización
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['demanda_normalizada'] = scaler.fit_transform(df[['demanda_energia']])

#Estandarización
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['demanda_estandarizada'] = scaler.fit_transform(df[['demanda_energia']])
