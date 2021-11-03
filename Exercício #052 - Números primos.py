""" Exercício Python 52: Faça um programa que leia um
número inteiro e diga se ele é ou não um número primo."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;92m-=-\033[m' * 15,
      '\n\033[97m               Números Primos'
      )
print('\033[1;92m-=-\033[m' * 15, '\n\033[97m')

numero = int(input('\n Informe um número: '))

total = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[1;92m', end=' ')
        total += 1

    else:
        print('\033[91m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\n\033[m \033[97mO número {numero} foi divisível {total} vezes.')

if total == 2:
    print(' E por isso ele é um número primo.\n')

else:
    print(' E por isso ele não é um número primo.\n')

print('\033[1;92m-=-\033[m' * 15,
      '\n\033[97m              Fim do programa'
      )
print('\033[1;92m-=-\033[m' * 15, '\n\033[97m')

# --------------------------------------------------------------------------


print('\033[1;34m↓ \033[m' * 8)
print('\033[1;4;38mNÚMEROS PRIMOS\033[m.')
print('\033[1;34m↑ \033[m' * 8)

number = int(input('\nInforme um número: '))
total = 0
for c in range(1, number + 1):
    if number % c == 0:
        print('\033[1;33m', end='')
        total = total + 1
    else:
        print('\033[1;31m', end='')
    print(f'{c} ', end='')
print(f'\n\n\033[mO número {number} foi divisível {total} vezes.')
if total == 2:
    print('\nE por isso é primo!\n\n  →  Fim  ←')
else:
    print('\nE por isso não é primo!\n\n  →  Fim  ←')
