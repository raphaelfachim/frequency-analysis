import src.controller.dados.importardados as importar
from src.model.modelos.variaveissensor import VariaveisSensor
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = VariaveisSensor("ai2", "ai3", "ai4", 10000)
    caminho = "C:\\Users\\rafas\\Desktop\\frequency-analysis\\src\\model\\data\\Dev4_1.txt"
    nome_raiz = "Dev4"

    b = importar.ler_dados_acelerometro(caminho, nome_raiz, a)
