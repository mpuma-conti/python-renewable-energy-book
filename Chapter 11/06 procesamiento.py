import numpy as np

# Simulación de lecturas en tiempo real (valores en bits del ADC)
lecturas = [512, 520, 518, 515, 525]  # Datos simulados del ADC
factor_conversion = 0.0033  # Conversión de bits a amperios

# Procesamiento en tiempo real
corrientes = [lectura * factor_conversion for lectura in lecturas]
promedio_corriente = np.mean(corrientes)

print(f"Corrientes medidas: {corrientes}")
print(f"Corriente promedio: {promedio_corriente:.2f} A")