import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Implementación recursiva de la FFT
def fft_recursive(x):
    N = len(x)
    if N <= 1:
        return x
    # FFT de las partes par e impar
    even = fft_recursive(x[0::2])
    odd = fft_recursive(x[1::2])
    # Calcula los factores twiddle
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    # Combina los resultados
    return [even[k] + T[k] for k in range(N // 2)] + \
           [even[k] - T[k] for k in range(N // 2)]

# Implementación recursiva de la IFFT
def ifft_recursive(X):
    N = len(X)
    if N <= 1:
        return X
    # IFFT de las partes par e impar
    even = ifft_recursive(X[0::2])
    odd = ifft_recursive(X[1::2])
    # Calcula los factores twiddle (con signo opuesto)
    T = [np.exp(2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    # Combina y divide por 2 (normalización)
    return [(even[k] + T[k]) / 2 for k in range(N // 2)] + \
           [(even[k] - T[k]) / 2 for k in range(N // 2)]

# Leer archivo de audio (entrada.wav)
rate, data = wavfile.read('wamba.wav')
# Si es estéreo, tomar solo un canal
if data.ndim > 1:
    data = data[:, 0]

# Rellenar con ceros hasta la siguiente potencia de 2
N = 2**int(np.ceil(np.log2(len(data))))
padded = np.zeros(N)
padded[:len(data)] = data

# Aplicar la FFT recursiva
X = fft_recursive(padded)

# Calcular las frecuencias correspondientes
freqs = np.fft.fftfreq(N, d=1/rate)

# Graficar el espectro de frecuencias
plt.figure(figsize=(12, 6))
plt.plot(freqs[:N//2], np.abs(X[:N//2]), color='green', linewidth=1.5)
plt.title('Espectro de Frecuencias', fontsize=16)
plt.xlabel('Frecuencia (Hz)', fontsize=14)
plt.ylabel('Magnitud', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Aplicar filtro pasabajas (por ejemplo, 4000 Hz) y acentuar graves (<500 Hz)
cutoff = 4000  # Hz
grave_boost = 2.0  # Factor de amplificación para graves
grave_limit = 500  # Hz

X_filtered = np.array(X)

# Eliminar frecuencias mayores al cutoff
X_filtered[np.abs(freqs) > cutoff] = 0

# Acentuar graves
grave_indices = np.abs(freqs) < grave_limit
X_filtered[grave_indices] *= grave_boost

# Aplicar la IFFT recursiva
y = ifft_recursive(X_filtered)
# Tomar la parte real y recortar al tamaño original
y = np.real(y[:len(data)]).astype(data.dtype)

# Guardar el resultado en un nuevo archivo de audio
wavfile.write('wamba_filtrada.wav', rate, y)