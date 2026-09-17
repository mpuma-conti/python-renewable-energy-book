import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Generación de datos simulados de vibración
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1.0, fs)
# Señal normal
vib_normal = 0.5 * np.sin(2 * np.pi * 50 * t)
# Señal con fallo (añadiendo una frecuencia adicional)
vib_fault = vib_normal + 0.2 * np.sin(2 * np.pi * 120 * t)

# Análisis de Fourier
def analisis_fft(vib_signal):
    N = len(vib_signal)
    yf = fft(vib_signal)
    xf = fftfreq(N, 1 / fs)[:N//2]
    return xf, 2.0/N * np.abs(yf[0:N//2])

xf_normal, yf_normal = analisis_fft(vib_normal)
xf_fault, yf_fault = analisis_fft(vib_fault)

# Visualización
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, vib_normal, label='Vibración Normal')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal de Vibración Normal')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, vib_fault, label='Vibración con Fallo', color='red')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal de Vibración con Fallo')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Análisis de frecuencia
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(xf_normal, yf_normal, label='FFT Vibración Normal')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.title('Espectro de Frecuencia - Vibración Normal')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(xf_fault, yf_fault, label='FFT Vibración con Fallo', color='red')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.title('Espectro de Frecuencia - Vibración con Fallo')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()