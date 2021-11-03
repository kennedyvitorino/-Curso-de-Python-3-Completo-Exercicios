"""Crie um programa que mostre na tela todos os
números pares que estão no intervalo entre 1 e 50. """
from time import sleep
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

print(f"    \033[30;107m{' Contando pares de 2 ':|^40}\033[m\n")

for cont in range(0, 51, 2):
    print(f'{cont}', end=' ')
    sleep(0.25)
print('→ Fim \n'
      f"    \033[30;107m{' Fim do Programa ':|^40}\033[m\n")

# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m                   Contagem de pares'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m')

for num in range(2, 51, 2):  # começa no 2, termina no 51, contando de 2 em 2.
    print(num, end=' ')
    sleep(0.30)

print('\n')
print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m                Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m')

# --------------------------------------------------------------------------

for n in range(2, 51, 2):
    print(n, end=' ')
    sleep(0.25)
print('Fim')
# for variavel_controle in range(2, 51, 2):
#     print(variavel_controle, end=' ')
# print('\033[1;32mFim do programa.\033[m')


# --------------------------------------------------------------------------

a = 4
b = 3
c = a + b
d = a - b
print(f'''\033[1;34m A Soma de {a} + {b} é igual a: {c}
 E a Subtração de {a} - {b} é igual a: {d}\033[m\n\n  \033[1;35mFim algoritmo!\n\033[m''')
