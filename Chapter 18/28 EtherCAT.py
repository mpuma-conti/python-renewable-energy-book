# Ejemplo de análisis de rendimiento de EtherCAT con Python
import time
import numpy as np

# Simulación de transmisión de paquetes
def transmitir_paquetes(num_paquetes):
    latencias = []
    for _ in range(num_paquetes):
        inicio = time.time()
        # Simulación de transmisión
        time.sleep(np.random.uniform(0.0001, 0.001))  # Latencia simulada entre 0.1ms y 1ms
        fin = time.time()
        latencias.append((fin - inicio) * 1000)  # Convertir a ms
    return latencias

# Transmitir 100 paquetes y calcular estadísticas
latencias = transmitir_paquetes(100)
print(f"Latencia promedio: {np.mean(latencias):.4f} ms")
print(f"Latencia máxima: {np.max(latencias):.4f} ms")
print(f"Latencia mínima: {np.min(latencias):.4f} ms")