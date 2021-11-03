"""Crie um pacote chamado utilidadesCeV que tenha dois módulos
internos chamados moeda e dado. Transfira todas as funções
utilizadas nos desafios 107, 108 e 109 para o primeiro
pacote e mantenha tudo funcionando."""


def aumentar(preco=0, taxa=0, formato=False):
    """
     -> Calcula o aumento de um determinado preço,
     retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar.
    :param taxa: qual é porcentagem do aumento.
    :param formato: quer a saída formatada ou nao?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda2='R$'):
    return f'{moeda2}{preco:>7.2f}'. replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('#===========#==========#===========#\n'
          '║        Resumo do Valor           ║\n'
          '#===========#==========#===========#\n'
          f'║ Preço analisado: \t{moeda(preco)}      ║\n'
          f'║ Dobro do preço: \t{dobro(preco, True)}      ║\n'
          f'║ Metade do preço: \t{metade(preco, True)}      ║\n'
          f'║ {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}      ║\n'
          f'║ {taxar}% de aumento: \t{diminuir(preco, taxar, True)}      ║\n'
          f'#===========#==========#===========# \n'
          f'║          Fim do programa         ║\n'
          f'#===========#==========#===========#')

