"""Exercício Python 074: Crie um programa que vai gerar cinco
números aleatórios e colocar em uma tupla. Depois disso, mostre
a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla."""
from random import randint

aleatorio = (randint(1, 11), randint(1, 11), randint(1, 11),
             randint(1, 11), randint(1, 11))

print(f' Os valores sorteados foram: ', end='')

for a in aleatorio:
    print(f'{a} ', end='')
print(f'\n O maior valor foi..... {max(aleatorio)}\n'
      f' O menor valor foi..... {min(aleatorio)}\n\n'
      f'   Fim do programa.\n')

# --------------------------------------------------------------------------

numeros = (randint(0, 11), randint(0, 11),
           randint(0, 11), randint(0, 11), randint(0, 11))

print(f'Os número sorteados foram: ', end='')

for n in numeros:
    print(f'{n} ', end='')

print(f'\nO maior numeral foi....... {max(numeros)}\n'
      f'E o menor numeral foi..... {min(numeros)}\n\n'
      f'     Fim do programa.')

# --------------------------------------------------------------------------
