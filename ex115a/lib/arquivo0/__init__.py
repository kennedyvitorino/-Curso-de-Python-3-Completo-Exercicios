from ex115a.lib.interface1 import *


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
        print(arquivo.read())

