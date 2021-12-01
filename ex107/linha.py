def linha(tamanho=50):
    return '\033[91m=\033[m' * tamanho


def cabecalho(texto):
    print(linha())
    print(texto.center(50))
    print(linha())
