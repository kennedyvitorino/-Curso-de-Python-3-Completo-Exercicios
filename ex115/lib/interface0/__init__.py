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


def linha(tam=38):
    return'-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(38))
    print(linha())


def menu(lista_opc):
    cabecalho('Menu Principal')
    cont = 1
    for item in lista_opc:
        print(f'\033[93m{cont}\033[m - \033[94m{item}\033[m')
        cont += 1
    print(linha())
    opc = leia_int('\033[92mSua Opção: \033[m')
    return opc
