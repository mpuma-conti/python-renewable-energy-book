# Parámetros
vida_util = 10  # años
tasa_descuento = 0.05  # 5%
beneficio_neto_anual = beneficio_anual - opex_anual

# Cálculo del NPV
npv = -capex
for t in range(1, vida_util + 1):
    npv += beneficio_neto_anual / (1 + tasa_descuento)**t

print(f"El valor presente neto (NPV) es de ${npv:.2f}")