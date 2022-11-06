import re


class VariaveisSensor:

    def __init__(self, var_x, var_y, var_z):
        self.x = var_x
        self.y = var_y
        self.z = var_z

    def set_tempo(self, tempo):
        tempo_float = []
        for t in tempo:
            tempo_float.append(float(re.sub("[^\d\.]", "", t)))

        self.tempo = tempo_float

    def set_dados_eixo_x(self, dados_x):
        self.dados_x = dados_x
        self.x_dc = dados_x[0]

    def set_dados_eixo_y(self, dados_y):
        self.dados_y = dados_y
        self.y_dc = dados_y[0]

    def set_dados_eixo_z(self, dados_z):
        self.dados_z = dados_z
        self.z_dc = dados_z[0]

    def get_taxa_amostragem(self):
        try:
            taxa_amostragem = 1/(self.tempo[1] - self.tempo[0])
            return taxa_amostragem
        except Exception as e:
            raise Exception("Não foi possível obter a taxa de amostragem >>", e)

    def get_quantidade_dados(self):
        try:
            tamanho = len(self.tempo)
            return tamanho
        except Exception as e:
            raise Exception("Não foi possível obter o tamanho do vetor de dados >>", e)