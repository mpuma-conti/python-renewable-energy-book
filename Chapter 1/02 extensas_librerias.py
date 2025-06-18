import numpy as np
import matplotlib.pyplot as plt

# Simulación de una señal de corriente alterna
frecuencia = 50  # en Hz
tiempo = np.linspace(0, 1, 500)  # 1 segundo de duración, 500 puntos
corriente = 10 * np.sin(2 * np.pi * frecuencia * tiempo)

# Cálculo de la transformada de Fourier
fft_resultado = np.fft.fft(corriente)
frecuencias = np.fft.fftfreq(len(tiempo), d=tiempo[1] - tiempo[0])

# Visualización del espectro de frecuencias
plt.plot(frecuencias, np.abs(fft_resultado))
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Espectro de la señal de corriente')
plt.show()