# Parámetros del transformador
perdida_nucleo = 100  # W
perdida_devanados = 150  # W

# Cálculo de pérdidas totales
perdida_total = perdida_nucleo + perdida_devanados
print(f"Pérdida total en el transformador: {perdida_total:.2f} W")