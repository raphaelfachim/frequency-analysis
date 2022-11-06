from scipy.signal import find_peaks


def descobre_maximos(x, y):
    maximos = find_peaks(y, height=5e-5, distance=1)
    return x[maximos[0]], maximos[1]['peak_heights']
