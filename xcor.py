from src.model.modelos.variaveissensor import VariaveisSensor as Sensor
import src.controller.dados.importardados as importar
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    sensor1 = Sensor("", "ai0", "")
    sensor2 = Sensor("", "ai1", "")

    # caminho = "C:\\Users\\raphael.fachim\\Desktop\\frequency-analysis\\src\\model\\data-09-05\\osciloscopio\\acquisitionDataRaphaelOsciloscopioSQW.txt"
    caminho = "C:\\Users\\raphael.fachim\\Desktop\\frequency-analysis\\src\\model\\data-11-05\\166cm-50kSas\\eixoZdist166cmapoios350kSas_3.txt"
    nome_raiz = "Dev1"

    sensor1 = importar.ler_dados_acelerometro(caminho, nome_raiz, sensor1)
    sensor2 = importar.ler_dados_acelerometro(caminho, nome_raiz, sensor2)


    sig1 = remover_dc(sensor1.dados_y, sensor1.y_dc)
    sig2 = remover_dc(sensor2.dados_y, sensor2.y_dc)

    sig1 = normalizar(sig1)
    sig2 = normalizar(sig2)

    time = sensor1.tempo

    fig, [ax1, ax2, ax3] = plt.subplots(3, 1, sharex=False)
    ax1.plot(time, sig1, label="Canal 1")
    ax1.plot(time, sig2, label="Canal 2")
    ax1.legend(loc='upper right', shadow=False, fontsize='x-small')
    ax1.grid(True)

    # "fatiar a imagem"
    # t_min = 4.5 # segundos
    # t_max = 5.5 # segundos

    # index_min = time.index(t_min)
    # index_max = time.index(t_max)

    # sig1 = sig1[index_min: index_max]
    # sig2 = sig2[index_min: index_max]
    # time = time[index_min: index_max]

    

    tempo_entre_amostras = time[1] - time[0]
    max_delay = 100 #ms
    max_delay_em_amostras = (max_delay / 1000) / tempo_entre_amostras

    lags = ax2.xcorr(sig1, sig2, normed=True, maxlags=None, lw=2)

    x_lags = lags[0]
    y_lags = lags[1]

    y_lags_max = np.max(y_lags)
    y_lags_max_index = np.where(y_lags == y_lags_max)
    amostra = x_lags[y_lags_max_index]

    # print(f"Sinal analisado entre {t_min} e {t_max} segundos")
    print(f"Lag (tempo entre amostras = {tempo_entre_amostras}): {np.abs(amostra * tempo_entre_amostras) * 1000} milissegundos")
    print(f"Y Lag máx = {y_lags_max}, na amostra: {amostra}")

    ax2.grid(True)

    ax3.plot(time, sig1, label="Canal 1")
    ax3.plot(time, sig2, label="Canal 2")
    ax3.legend(loc='upper right', shadow=False, fontsize='x-small')
    ax3.grid(True)

    plt.show()

def remover_dc(vetor: np.array, dc: float):
    if(dc):
        return np.subtract(vetor, dc)
    else:
        media = np.mean(vetor)
        return np.subtract(vetor, media)

def normalizar(vetor: np.array):
    print(f"maximo : {np.max(np.abs(vetor))}")
    return vetor / np.max(np.abs(vetor))


if __name__ == "__main__":
    main()