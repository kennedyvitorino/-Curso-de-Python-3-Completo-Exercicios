"""Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno."""


def area(larg, compr):
    a = larg * compr
    print(f'A área de um terreno {larg} x {compr} é de {a}m²')


print('=' * 35)
print('     Controle de Terrenos')
print('=' * 35)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

# -------------------------------------------------------------------------------


def area(largura, comprimento):
    ar = largura * comprimento
    print('\033[1;93m-_\033[m' * 21)
    print(f'A área de um terreno \033[1;94m{largura}\033[m x \033[1;94m{comprimento}\033[m é de \033[1;94m{ar}\033[mm².')


# Programa Principal
print('\033[1;93m○\033[m' * 28)
print('           Controle de Terrenos')
print('\033[1;93m○\033[m' * 28)

largu = float(input('Largura (m): '))
compri = float(input('Comprimento (m): '))

area(largu, compri)
