import src.controller.dados.importardados as importar
import src.controller.frequencia.fft as fft
import numpy as np
import matplotlib.pyplot as plt
from src.model.modelos.variaveissensor import VariaveisSensor
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    acel = VariaveisSensor("ai2", "ai3", "ai4")
    caminho = "C:\\Users\\rafas\\Desktop\\frequency-analysis\\src\\model\\data\\Dev4_1.txt"
    nome_raiz = "Dev4"

    acel = importar.ler_dados_acelerometro(caminho, nome_raiz, acel)

    # f = 20 hz
    # N = 1000 samples/s
    # t = 5 s
    f = 20
    N = 1000
    Lx = 1000*5
    omega = 2.0*np.pi*f

    t = np.linspace(0, 5, Lx)

    x = 5*np.sin(omega*t)

    f, espectro = fft.fft(x, quantidade_amostras=Lx, tempo_amostragem=1/N)

    plt.figure(1)
    plt.plot(f, espectro)
    plt.title("FFT")

    plt.show()
