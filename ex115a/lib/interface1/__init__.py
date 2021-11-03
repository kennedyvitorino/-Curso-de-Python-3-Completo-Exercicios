def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):  # tratamento de EXCEÇÕES
            print('\033[91m Erro: por favor digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[91mEntrada de dados interrompida pelo usuário\033[m')
            continue
        else:
            return numero


def linha(tamanho=38):
    return '=' * tamanho


def cabecalho(texto):
    print(linha())
    print(texto.center(38))
    print(linha())


def menu(lista_opc):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista_opc:
        print(f'\033[93m{contador}\033[m - \033[94m{item}\033[m')
        contador += 1
    print(linha())
    opc = leia_int('\033[92mSua Opção: \033[m')
    return opc
