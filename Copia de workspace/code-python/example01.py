import numpy as np
import matplotlib.pyplot as plt

import jappy_utils as jutils
#jutils.setWD('/code-python')

def main():
    # Parámetros
    fs = 1000  # Frecuencia de muestreo
    t = np.linspace(0, 1, fs)  # Tiempo de 0 a 1 segundo

    # Frecuencias
    f_m = 2  # Frecuencia de la señal moduladora (Hz)
    f_c = 10  # Frecuencia de la señal portadora (Hz)

    # Señales
    moduladora = np.sin(2 * np.pi * f_m * t)  # Señal moduladora
    portadora = np.sin(2 * np.pi * f_c * t)  # Señal portadora

    # Señal modulada
    modulada = (1 + moduladora) * portadora  # Modulación de amplitud

    # Gráficos
    plt.figure(figsize=(12, 6))

    # Señal moduladora
    plt.subplot(3, 1, 1)
    plt.plot(t, moduladora, label='Señal Moduladora (f_m=2 Hz)')
    plt.title('Señal Moduladora')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid()
    plt.legend()

    # Señal portadora
    plt.subplot(3, 1, 2)
    plt.plot(t, portadora, label='Señal Portadora (f_c=10 Hz)', color='orange')
    plt.title('Señal Portadora')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid()
    plt.legend()

    # Señal modulada
    plt.subplot(3, 1, 3)
    plt.plot(t, modulada, label='Señal Modulada', color='green')
    plt.title('Señal Modulada')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid()
    plt.legend()

    plt.tight_layout()
    
    plt.savefig('senal_modulada.png')  # Guarda la imagen en un archivo
    plt.close()  # Cierra la figura


if __name__ == "__main__":
    main()
