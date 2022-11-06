import src.controller.dados.importardados as importar
import src.controller.frequencia.fft as fft
import numpy as np
import matplotlib.pyplot as plt
from src.model.modelos.variaveissensor import VariaveisSensor
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    acel = VariaveisSensor("ai2", "ai3", "ai4")
    caminho = "C:\\Users\\rafas\\Desktop\\frequency-analysis\\src\\model\\data\\Dev4_7.txt"
    nome_raiz = "Dev4"

    acel = importar.ler_dados_acelerometro(caminho, nome_raiz, acel)

    f, espectro = fft.fft(acel.dados_x,
                          quantidade_amostras=acel.get_quantidade_dados(), tempo_amostragem=1/acel.get_taxa_amostragem())

    plt.figure(1)
    plt.plot(f, espectro)
    plt.title("FFT")

    plt.show()
