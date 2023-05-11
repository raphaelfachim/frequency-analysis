from src.model.modelos.variaveissensor import VariaveisSensor
import src.controller.dados.importardados as importar
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp, butter, lfilter
import numpy as np

def butter_bandpass(lowcut, highcut, fs, order=5):
    return butter(order, [lowcut, highcut], fs=fs, btype='band')

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_lowpass(fcut, fs, order=5):
    return butter(order, fcut, fs=fs, btype='low')

def butter_lowpass_filter(data, fcut, fs, order=5):
    b, a = butter_lowpass(fcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def main():
    caminho = "C:\\Users\\raphael.fachim\\Desktop\\frequency-analysis\\src\\model\\data-15-12\\Dev4_24.txt"
    nome_raiz = "Dev4"

    # x : ai2, ai10
    # y : ai3, ai11
    # z : ai4, ai12
    sensor1 = VariaveisSensor("", "ai3", "")
    sensor2 = VariaveisSensor("", "ai11", "")

    sensor1 = importar.ler_dados_acelerometro(caminho=caminho, nome_raiz=nome_raiz, variaveis_sensor=sensor1)
    sensor2 = importar.ler_dados_acelerometro(caminho=caminho, nome_raiz=nome_raiz, variaveis_sensor=sensor2)


    sensor1.set_dados_eixo_z(sensor1.dados_y)
    # a = [x - 13 for x in a]
    sensor1.dados_y = [x - sensor1.y_dc for x in sensor1.dados_y]
    sensor2.dados_y = [x - sensor2.y_dc for x in sensor2.dados_y]

    # t1 = 5.8    # segundos
    # t2 = 8  # segundos

    # 100 k Sa/s
    # 1 s -> 100 000 amostras -> 1e5 amostras

    # t_novo = sensor1.tempo[int(t1 * 1e5): int(t2 * 1e5)]

    # sensor1.dados_y = sensor1.dados_y[int(t1 * 1e5): int(t2 * 1e5)]
    # sensor2.dados_y = sensor2.dados_y[int(t1 * 1e5): int(t2 * 1e5)]

    low = 160
    high = 400

    # sens1_filtro = butter_bandpass_filter(sensor1.dados_y, 2 * np.pi * low, 2 * np.pi * high,
    #                             sensor1.get_taxa_amostragem(), order=5)
    # sens2_filtro = butter_bandpass_filter(sensor2.dados_y, 2 * np.pi * low, 2 * np.pi * high,
    #                            sensor2.get_taxa_amostragem(), order=5)

    plt.figure(1)
    plt.plot(sensor1.tempo, sensor1.dados_y, sensor1.tempo, sensor2.dados_y)
    plt.legend(["Acelerômetro próximo", "Acelerômetro distante"])
    plt.title("Analise no tempo sensores")

    sinal_analitico1 = hilbert(sensor1.dados_y)
    envelope1 = np.abs(sinal_analitico1)

    sinal_analitico2 = hilbert(sensor2.dados_y)
    envelope2 = np.abs(sinal_analitico2)

    # plt.figure(2)
    # plt.plot(t_novo, envelope1, label="envelope1")
    # plt.plot(t_novo, envelope2, label="envelope2")
    # plt.title("Envelope da leitura do sensor 1")

    # plt.figure(2)
    # plt.plot(sensor2.tempo, sensor2.dados_z)
    # plt.title("Analise no tempo sensor 2")
    plt.show()
    print("End of program")

if __name__ == '__main__':
    main()