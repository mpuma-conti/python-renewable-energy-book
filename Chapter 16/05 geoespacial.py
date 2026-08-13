import geopandas as gpd

# Cargar datos geoespaciales
gdf = gpd.read_file('mapa_impacto_ambiental.shp')

# Graficar el mapa de impacto ambiental
gdf.plot(column='Impacto', cmap='coolwarm', legend=True)
plt.title('Impacto Ambiental de Energía Renovable')
plt.show()