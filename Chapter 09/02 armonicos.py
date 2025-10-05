import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Generar una señal con armónicos
fs = 1000  # Frecuencia de muestreo
t = np.linspace(0, 1, fs, endpoint=False)  # Tiempo
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 150 * t)

# Transformada rápida de Fourier
fft_signal = fft(signal)
frequencies = np.fft.fftfreq(len(t), 1/fs)

# Graficar
plt.figure(figsize=(10, 5))
plt.plot(frequencies[:fs//2], np.abs(fft_signal)[:fs//2])
plt.title("Análisis de Armónicos en la Señal")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()