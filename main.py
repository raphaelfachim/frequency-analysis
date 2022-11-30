import os

import src.controller.dados.importardados as importar
import src.controller.dados.exportardados as exportador
import src.controller.frequencia.fft as fft
import src.controller.analysis.descobrirmaximos as maximos
import matplotlib.pyplot as plt
import datetime
from src.model.modelos.variaveissensor import VariaveisSensor

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    timestamp = str(datetime.datetime.now()).replace(".", "-").replace(":", "-").replace(" ", "-")
    conteudo = ""
    acel = VariaveisSensor("ai2", "ai3", "ai4")
    acel_2 = VariaveisSensor("ai10", "ai11", "ai12")
    nome_raiz = "Dev4"
    amostra = 7
    limite = 16

    os.makedirs(timestamp)

    while amostra <= limite:
        caminho = "C:\\Users\\rafas\\Desktop\\frequency-analysis\\src\\model\\data\\Dev4_" + str(amostra) + ".txt"

        acel = importar.ler_dados_acelerometro(caminho, nome_raiz, acel)
        acel_2 = importar.ler_dados_acelerometro(caminho, nome_raiz, acel_2)

        f, espectro = fft.fft(acel.dados_x,
                              quantidade_amostras=acel.get_quantidade_dados(),
                              tempo_amostragem=1 / acel.get_taxa_amostragem())
        max_x, max_y = maximos.descobre_maximos(f, espectro)

        f_2, espectro_2 = fft.fft(acel_2.dados_x,
                                  quantidade_amostras=acel_2.get_quantidade_dados(),
                                  tempo_amostragem=1 / acel_2.get_taxa_amostragem())
        max_x_2, max_y_2 = maximos.descobre_maximos(f_2, espectro_2)

        plt.figure(amostra)
        plt.plot(f, espectro, f_2, espectro_2)
        plt.scatter(max_x, max_y, color="r", s=15, marker="D", label="Maximos")
        plt.scatter(max_x_2, max_y_2, color="g", s=15, marker="D", label="Maximos")
        plt.title("FFT dos sinais coletados perto (azul) e longe (amarelo) do sensor")

        nome_figura = "C:\\Users\\rafas\\Desktop\\frequency-analysis\\{0}\\amostra-{1}.{2}".format(timestamp,
                                                                                                   str(amostra), "png")

        conteudo += "Arquivo da amostra : [{0}] \nPicos de frequência [Hz] = {1}\n" \
                    "Picos de frequência (acelerômetro distante)[Hz] = {2}\n\n".format(amostra, max_x, max_x_2)

        # nome_figura = nome_figura.replace(" ", "-")

        plt.savefig(nome_figura)

        amostra += 1

    nome_texto = "C:\\Users\\rafas\\Desktop\\frequency-analysis\\{0}\\relatorio.{1}".format(timestamp,
                                                                                            "txt")
    exportador.exportar_dados(nome_arquivo=nome_texto, conteudo=conteudo, criar=True)
    plt.show()
