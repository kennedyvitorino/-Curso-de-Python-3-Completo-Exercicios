"""Crie um programa onde 4 jogadores joguem
um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado."""
# Alt + 220 ▄
# Alt + 219 █
# ALT + 205 ═

from random import randint
from time import sleep
from operator import itemgetter


jogo_dict = {'O jogador No 1': randint(1, 6),
             'O jogador No 2': randint(1, 6),
             'O jogador No 3': randint(1, 6),
             'O jogador No 4': randint(1, 6)}

rank = list()

print('Sorteando valores...')
sleep(0.5)

for kei, valor in jogo_dict.items():
    print(f'{kei} tirou {valor} no dado.')
    sleep(0.5)

rank = sorted(jogo_dict.items(), key=itemgetter(1), reverse=True)

print('▄' * 31)
print('  == Ranking dos Jogadores ==')
print('▀' * 31)

for indice, valor in enumerate(rank):
    print(f'{indice + 1}º lugar: {valor[0]} com {valor[1]}')
