import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
frecuencia_muestreo = 10000  # Hz
duracion = 1  # segundos
frecuencia_signal = 50  # Hz, frecuencia nominal de la señal (valor de ejemplo)

# Generación de una señal de corriente alterna (sinusoidal)
t = np.linspace(0, duracion, int(frecuencia_muestreo * duracion), endpoint=False)
senal = np.sin(2 * np.pi * frecuencia_signal * t)

# Aplicar la FFT para obtener el espectro de frecuencia
frecuencias = np.fft.fftfreq(len(t), 1/frecuencia_muestreo)
espectro = np.abs(np.fft.fft(senal))

# Encontrar la frecuencia dominante (más alta amplitud)
frecuencia_dominante = np.abs(frecuencias[np.argmax(espectro)])

# Mostrar los resultados
print(f"La frecuencia dominante es: {frecuencia_dominante:.2f} Hz")

# Graficar la señal y el espectro de frecuencia
plt.figure(figsize=(10, 6))

# Señal en el tiempo
plt.subplot(2, 1, 1)
plt.plot(t, senal)
plt.title("Señal de Corriente Alterna")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")

# Espectro de Frecuencia
plt.subplot(2, 1, 2)
plt.plot(frecuencias[:len(frecuencias)//2], espectro[:len(frecuencias)//2])
plt.title("Espectro de Frecuencia")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")

plt.tight_layout()
plt.show()