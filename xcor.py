from src.model.modelos.variaveissensor import VariaveisSensor as Sensor
import src.controller.dados.importardados as importar
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    sensor1 = Sensor("", "ai0", "")
    sensor2 = Sensor("", "ai1", "")

    caminho = "D:\\Users\\rafas\\Desktop\\frequency-analysis\\src\\model\\data-20-04\\Dev1_15.txt"
    nome_raiz = "Dev1"

    sensor1 = importar.ler_dados_acelerometro(caminho, nome_raiz, sensor1)
    sensor2 = importar.ler_dados_acelerometro(caminho, nome_raiz, sensor2)

    sig1 = sensor1.dados_y
    sig2 = np.roll(sensor2.dados_y, 300)
    time = sensor1.tempo

    fig, [ax1, ax2, ax3] = plt.subplots(3, 1, sharex=False)
    ax1.plot(time, sig1, label="Sensor próximo")
    ax1.plot(time, sig2, label="Sensor distante")
    ax1.legend(loc='upper right', shadow=False, fontsize='x-small')
    ax1.grid(True)

    # "fatiar a imagem"
    t_min = 6.5 # segundos
    t_max = 7.5 # segundos

    index_min = time.index(t_min)
    index_max = time.index(t_max)

    sig1 = sig1[index_min: index_max]
    sig2 = sig2[index_min: index_max]
    time = time[index_min: index_max]

    print(f"Index min : {index_min}, Index max : {index_max}")

    tempo_entre_amostras = time[1] - time[0]
    max_delay = 100 #ms
    max_delay_em_amostras = (max_delay / 1000) / tempo_entre_amostras

    lags = ax2.xcorr(sig1, sig2, normed=True, maxlags=None, lw=2)
    ax2.grid(True)

    ax3.plot(time, sig1, label="Sensor próximo")
    ax3.plot(time, sig2, label="Sensor distante")
    ax3.legend(loc='upper right', shadow=False, fontsize='x-small')
    ax3.grid(True)

    plt.show()

if __name__ == "__main__":
    main()