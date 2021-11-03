from ex115b.lib.interface2 import *


def arquivo_existe(nome):
    try:
        arquivo = open(nome, 'rt')  # 'rt' Read Text: tentar abrir arquivo como TEXTO
        arquivo.close()

    except FileNotFoundError:
        return False

    else:
        return True


def criar_arquivo(nome):
    try:
        arquivo = open(nome, 'wt+')  # 'wt+' Escrever arquivo de texto, caso não o arquivo não exista ele CRIA.
        arquivo.close()

    except (Exception,):
        print('Houve um ERRO na criação do seu arquivo!')

    else:
        print(f'arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except (Exception,):
        print(f'ERRO ao tentar ler o arquivo {nome}')

    else:
        cabecalho('PESSOAS CADASTRADAS')

        for linhaa in arquivo:
            dado = linhaa.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        arquivo.close()


def cadastrar(arq, nome='DESCONHECIDO', idade=0):
    try:
        arquivo = open(arq, 'at')
    except (Exception,):
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except (Exception,):
            print('Houve um ERRO na hora deescrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            arquivo.close()
