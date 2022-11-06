import numpy as np
from typing import List


def fft(sinal: List[float], quantidade_amostras: int, tempo_amostragem: float):
    frequencias = np.fft.fftfreq(quantidade_amostras, tempo_amostragem)
    modulo_espectro = 2*np.abs(np.fft.fft(sinal)/quantidade_amostras)

    mascara = frequencias > 0

    return frequencias[mascara], modulo_espectro[mascara]
