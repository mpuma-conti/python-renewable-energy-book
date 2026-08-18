from py4j.java_gateway import JavaGateway

# Iniciar la conexión con OpenLCA a través de Py4j
gateway = JavaGateway()  # Esto abre una conexión con la API de OpenLCA

# Acceder a la base de datos de OpenLCA
model = gateway.entry_point.getModel("solar_panel_system")  # Nombre del modelo de energía solar

# Cargar el proyecto LCA
project = model.loadProject("path_to_project_file")  # Ruta al archivo del proyecto de OpenLCA

# Realizar los cálculos de impacto ambiental
impact_calculator = project.createImpactCalculator()
results = impact_calculator.calculate()

# Mostrar los resultados
print("Resultados del Análisis de Ciclo de Vida para el Sistema Fotovoltaico:")
for impact, value in results.items():
    print(f"{impact}: {value} puntos de impacto ambiental")