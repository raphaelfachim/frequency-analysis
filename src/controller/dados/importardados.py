import pandas as pd
from typing import List
from src.model.modelos.variaveissensor import VariaveisSensor


def ler_dados_acelerometro(caminho: str, nome_raiz: str, variaveis_sensor: VariaveisSensor):
    cabecalho = []

    variaveis_sensor.x = nome_raiz + "_" + variaveis_sensor.x
    variaveis_sensor.y = nome_raiz + "_" + variaveis_sensor.y
    variaveis_sensor.z = nome_raiz + "_" + variaveis_sensor.z

    try:
        dados = pd.read_csv(caminho)

        variaveis_sensor.set_tempo(tempo=dados["Time"])

        variaveis_sensor.set_dados_eixo_x(dados_x=dados[variaveis_sensor.x].tolist())
        variaveis_sensor.set_dados_eixo_y(dados_y=dados[variaveis_sensor.y].tolist())
        variaveis_sensor.set_dados_eixo_z(dados_z=dados[variaveis_sensor.z].tolist())

        return variaveis_sensor
    except Exception as e:
        print("Erro ao processar arquivo! >>", e)
