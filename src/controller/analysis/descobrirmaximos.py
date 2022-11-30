import math

from scipy.signal import find_peaks


def descobre_maximos(x, y):
    distancia = math.floor(25 / (x[1] - x[0]))  # faixas de 50 Hz (25 para cada lado)
    maximos = find_peaks(y, height=5e-5, distance=distancia)
    return x[maximos[0]], maximos[1]['peak_heights']
