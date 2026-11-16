
# ============================================================
# PROYECTO: DISEÑO DE FILTROS DIGITALES
# Filtros pasa bajos, pasa altos y pasa bandas
# Librerías: NumPy, SciPy y Matplotlib
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ------------------------------------------------------------
# 1. DEFINICIÓN DE LA SEÑAL DE ENTRADA
# ------------------------------------------------------------

fs = 1000             # Frecuencia de muestreo en Hz
duracion = 2           # Duración de la señal en segundos
t = np.arange(0, duracion, 1/fs)

# Señal compuesta por tres frecuencias
f1 = 5                 # Frecuencia baja
f2 = 50                # Frecuencia media
f3 = 120               # Frecuencia alta

senal_limpia = (
    np.sin(2 * np.pi * f1 * t)
    + 0.7 * np.sin(2 * np.pi * f2 * t)
    + 0.5 * np.sin(2 * np.pi * f3 * t)
)

# Se agrega ruido blanco para simular una señal real
np.random.seed(42)
ruido = 0.5 * np.random.randn(len(t))
senal_ruidosa = senal_limpia + ruido

# ------------------------------------------------------------
# 2. DISEÑO DE LOS FILTROS IIR BUTTERWORTH
# ------------------------------------------------------------

orden = 4

# Filtro pasa bajos: conserva frecuencias inferiores a 20 Hz
sos_bajos = signal.butter(
    orden, 20, btype="lowpass",
    fs=fs, output="sos"
)

# Filtro pasa altos: conserva frecuencias superiores a 40 Hz
sos_altos = signal.butter(
    orden, 40, btype="highpass",
    fs=fs, output="sos"
)

# Filtro pasa bandas: conserva frecuencias entre 40 y 80 Hz
sos_bandas = signal.butter(
    orden, [40, 80], btype="bandpass",
    fs=fs, output="sos"
)

# ------------------------------------------------------------
# 3. APLICACIÓN DE LOS FILTROS
# ------------------------------------------------------------

# filtfilt aplica el filtrado hacia adelante y hacia atrás,
# evitando el desfase neto en la señal fuera de los bordes.
salida_bajos = signal.sosfiltfilt(sos_bajos, senal_ruidosa)
salida_altos = signal.sosfiltfilt(sos_altos, senal_ruidosa)
salida_bandas = signal.sosfiltfilt(sos_bandas, senal_ruidosa)

# ------------------------------------------------------------
# 4. GRAFICAR LAS SEÑALES ANTES Y DESPUÉS DEL FILTRADO
# ------------------------------------------------------------

fig, ejes = plt.subplots(4, 1, figsize=(12, 12))

ejes[0].plot(t, senal_ruidosa, label="Señal con ruido")
ejes[0].plot(t, senal_limpia, label="Señal limpia", alpha=0.8)
ejes[0].set_title("Señal original y señal con ruido")
ejes[0].set_ylabel("Amplitud")
ejes[0].legend()
ejes[0].grid(True)

ejes[1].plot(t, salida_bajos)
ejes[1].set_title("Filtro pasa bajos (20 Hz)")
ejes[1].set_ylabel("Amplitud")
ejes[1].grid(True)

ejes[2].plot(t, salida_altos)
ejes[2].set_title("Filtro pasa altos (40 Hz)")
ejes[2].set_ylabel("Amplitud")
ejes[2].grid(True)

ejes[3].plot(t, salida_bandas)
ejes[3].set_title("Filtro pasa bandas (40-80 Hz)")
ejes[3].set_xlabel("Tiempo (s)")
ejes[3].set_ylabel("Amplitud")
ejes[3].grid(True)

plt.tight_layout()
plt.savefig("comparacion_senales.png", dpi=300)
plt.show()

# ------------------------------------------------------------
# 5. RESPUESTA EN FRECUENCIA DE LOS FILTROS
# ------------------------------------------------------------

f_bajos, h_bajos = signal.sosfreqz(
    sos_bajos, worN=2048, fs=fs
)
f_altos, h_altos = signal.sosfreqz(
    sos_altos, worN=2048, fs=fs
)
f_bandas, h_bandas = signal.sosfreqz(
    sos_bandas, worN=2048, fs=fs
)

plt.figure(figsize=(12, 6))

plt.plot(
    f_bajos,
    20 * np.log10(np.maximum(np.abs(h_bajos), 1e-10)),
    label="Pasa bajos"
)
plt.plot(
    f_altos,
    20 * np.log10(np.maximum(np.abs(h_altos), 1e-10)),
    label="Pasa altos"
)
plt.plot(
    f_bandas,
    20 * np.log10(np.maximum(np.abs(h_bandas), 1e-10)),
    label="Pasa bandas"
)

plt.title("Respuesta en frecuencia de los filtros")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.xlim(0, 200)
plt.ylim(-80, 5)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("respuesta_frecuencia.png", dpi=300)
plt.show()

# ------------------------------------------------------------
# 6. ANÁLISIS DE RESULTADOS
# ------------------------------------------------------------

def calcular_rms(senal):
    """Calcula el valor RMS de una señal."""
    return np.sqrt(np.mean(senal**2))

print("\n===== RESULTADOS DEL PROYECTO =====")
print(f"RMS de la señal limpia:   {calcular_rms(senal_limpia):.4f}")
print(f"RMS de la señal con ruido: {calcular_rms(senal_ruidosa):.4f}")
print(f"RMS después del pasa bajos: {calcular_rms(salida_bajos):.4f}")
print(f"RMS después del pasa altos: {calcular_rms(salida_altos):.4f}")
print(f"RMS después del pasa bandas: {calcular_rms(salida_bandas):.4f}")

print("\nGráficas guardadas correctamente.")
