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
    caminho = "C:\\Users\\rafas\\Desktop\\frequency-analysis\\src\\model\\data-15-12\\Dev4_9.txt"
    nome_raiz = "Dev4"

    sensor1 = VariaveisSensor("ai2", "", "")
    sensor2 = VariaveisSensor("ai10", "", "")

    sensor1 = importar.ler_dados_acelerometro(caminho=caminho, nome_raiz=nome_raiz, variaveis_sensor=sensor1)
    sensor2 = importar.ler_dados_acelerometro(caminho=caminho, nome_raiz=nome_raiz, variaveis_sensor=sensor2)


    sensor1.set_dados_eixo_x(sensor1.dados_x)
    # a = [x - 13 for x in a]
    sensor1.dados_x = [x - sensor1.x_dc for x in sensor1.dados_x]
    sensor2.dados_x = [x - sensor2.x_dc for x in sensor1.dados_x]

    low = 160
    high = 400

    sens1_filtro = butter_bandpass_filter(sensor1.dados_x, 2 * np.pi * low, 2 * np.pi * high,
                                          sensor1.get_taxa_amostragem(), order=5)
    sens2_filtro = butter_bandpass_filter(sensor2.dados_x, 2 * np.pi * low, 2 * np.pi * high,
                                          sensor2.get_taxa_amostragem(), order=5)

    plt.figure(1)
    plt.plot(sensor1.tempo, sensor1.dados_x, label="original")
    plt.plot(sensor1.tempo, sens1_filtro, label="filtrado")
    plt.title("Analise no tempo sensor 1")

    sinal_analitico1 = hilbert(sens1_filtro)
    envelope1 = np.abs(sinal_analitico1)

    sinal_analitico2 = hilbert(sens2_filtro)
    envelope2 = np.abs(sinal_analitico2)

    plt.figure(2)
    plt.plot(sensor1.tempo, envelope1, label="envelope1")
    plt.plot(sensor2.tempo, envelope2, label="envelope2")
    plt.title("Envelope da leitura do sensor 1")

    # plt.figure(2)
    # plt.plot(sensor2.tempo, sensor2.dados_x)
    # plt.title("Analise no tempo sensor 2")
    plt.show()
    print("End of program")

if __name__ == '__main__':
    main()