# Datos de energía (en kWh)
energia_generada = 10000
energia_facturada = 9500

# Cálculo de pérdidas no técnicas
perdida_no_tecnica = energia_generada - energia_facturada
porcentaje_perdida = (perdida_no_tecnica / energia_generada) * 100

print(f"Pérdida no técnica: {perdida_no_tecnica} kWh ({porcentaje_perdida:.2f}%)")