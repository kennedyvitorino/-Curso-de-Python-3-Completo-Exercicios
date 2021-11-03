""" Exercício Python 060: Faça um programa que
leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120 """
from time import sleep
from math import factorial
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m              Criando um menú de opções'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

num = int(input(' Digite um número para calcular seu Factorial: '))

cont = num  # contador do fatorial
fatorial = 1

print(f'\n Calculando o fatorial de {cont} logo abaixo!')

while cont > 0:  # Enquanto o contador for menor que 0...
    # for c in range(num, 0, -1): # é melhor usar o for quando ja se sabe o limite.
    print(f' \033[1;95m{cont}', end='')
    print(' x' if cont > 1 else ' = ', end='')  # mostre o x SE o fac for maior que o 1, se não mostre um =

    fatorial *= cont
    cont -= 1

print(f'{fatorial}\n\033[m')

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m                   Fim do programa'
      )
print('\033[1;92m-=-\033[m' * 18)

# --------------------------------------------------------------------------


# n = int(input('Digite um número para calcular seu Factorial:  '))
# f = factorial(n)
# sleep(0.8)
# print(f)
#
# # --------------------------------------------------------------------------
#
#
num = int(input('Digite um número para calcular seu Factorial: '))
c = num  # fac = contador
fac = 1
print(f'Calculando {c}! = ', end='')
while c > 0:  # Enquanto o contador for menor que 0...
    #    # for c in range(num, 0, -1): # é melhor usar o for quando ja se sabe o limite.
    print(f'\033[31m{c}', end='')
    print(' x ' if c > 1 else ' = ', end='\033[m')  # mostre o x SE o fac for maior que o 1, se não mostre um =
    sleep(0.5)
    fac *= c
    c -= 1
print(fac)
