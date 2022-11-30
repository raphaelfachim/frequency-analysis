import pandas as pd
from src.model.modelos.variaveissensor import VariaveisSensor


def ler_dados_acelerometro(caminho: str, nome_raiz: str, variaveis_sensor: VariaveisSensor):
    dados_x = nome_raiz + "_" + variaveis_sensor.x
    dados_y = nome_raiz + "_" + variaveis_sensor.y
    dados_z = nome_raiz + "_" + variaveis_sensor.z

    try:
        dados = pd.read_csv(caminho)

        variaveis_sensor.set_tempo(tempo=dados["Time"])
        variaveis_sensor.set_dados_eixo_x(dados_x=dados[dados_x].tolist())
        variaveis_sensor.set_dados_eixo_y(dados_y=dados[dados_y].tolist())
        variaveis_sensor.set_dados_eixo_z(dados_z=dados[dados_z].tolist())

        return variaveis_sensor
    except Exception as e:
        print("Erro ao processar arquivo! >>", e)
