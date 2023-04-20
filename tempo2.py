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
    acel = VariaveisSensor("", "", "ai4")
    acel_2 = VariaveisSensor("", "", "ai12")
    nome_raiz = "Dev4"
    amostra = 13
    limite = 25

    os.makedirs(timestamp)

    while amostra <= limite:
        print("lendo amostra {}".format(amostra))
        caminho = "C:\\Users\\rafas\\Desktop\\frequency-analysis\\src\\model\\data-15-12\\Dev4_" + str(amostra) + ".txt"

        acel = importar.ler_dados_acelerometro(caminho, nome_raiz, acel)
        acel_2 = importar.ler_dados_acelerometro(caminho, nome_raiz, acel_2)

        nome_figura = "C:\\Users\\rafas\\Desktop\\frequency-analysis\\{0}\\amostra-{1}.{2}".format(timestamp,
                                                                                                   str(amostra), "png")


        # nome_figura = nome_figura.replace(" ", "-")

        plt.savefig(nome_figura)
        plt.figure(amostra)
        plt.plot(acel.tempo, acel.dados_z, acel_2.tempo, acel_2.dados_z)
        plt.title("Analise no tempo sensores")
        amostra += 1
    plt.show()
