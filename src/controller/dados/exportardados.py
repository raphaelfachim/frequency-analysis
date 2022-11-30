def exportar_dados(nome_arquivo: str, conteudo: str, criar: bool):
    flag_criar = "a"
    if criar:
        flag_criar = "x"
    f = open(nome_arquivo, flag_criar)
    print("noeee", nome_arquivo, flag_criar)
    f.write(conteudo)
    f.close()
