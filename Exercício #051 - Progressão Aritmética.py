""" Desenvolva um programa que leia o
primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros
termos dessa progressão."""
from time import sleep
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;92m-=-\033[m' * 12,
      '\n\033[97m       10 Termos de uma PA'
      )
print('\033[1;92m-=-\033[m' * 12, '\n\033[97m')

termo1 = int(input('\n Primeiro termo:....'))  # começar por qual número
razao = int(input(' Segundo termo:.....'))  # pulando de 2 em 2, 3 em 3, etc...

decimoT = termo1 + (10 - 1) * razao  # décimo termo.

for c in range(termo1, decimoT + razao, razao):
    print(f' {c}', end=' → ')

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m                  Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m')

# --------------------------------------------------------------------------

#
# sleep(0.5)
# print('\033[1;31m-=\033[m' * 11)
# sleep(0.5)
# print('\033[1;34m 10 TERMOS DE UMA PA.\033[m')
# sleep(0.5)
#
# print('\033[1;31m-=\033[m' * 11)
# first = int(input('\nFirst term: '))  # começar por qual numero
# reason = int(input('Reason: '))  # pulando de 2 em 2, 3 em 3, etc...
# tenth = first + (10 - 1) * reason  # décimo termo.
# for c in range(first, tenth + reason, reason):
#     print(f'{c}', end=' → ')
# print('\033[1;31m\n\nAcabou.\033[m')
