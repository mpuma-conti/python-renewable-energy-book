# Datos iniciales
capex = 10000  # Costo de inversión inicial en dólares
opex_anual = 500  # Costo de operación anual
beneficio_anual = 2000  # Ahorro anual en dólares

# Retorno de inversión
roi = capex / (beneficio_anual - opex_anual)
print(f"El retorno de inversión es de {roi:.2f} años.")