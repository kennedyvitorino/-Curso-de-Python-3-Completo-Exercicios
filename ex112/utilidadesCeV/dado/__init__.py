def leia_dinheiro(msg):
    valido = False

    while not valido:
        entrada = str(input(msg)).replace(',', '.')

        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[1;91mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
