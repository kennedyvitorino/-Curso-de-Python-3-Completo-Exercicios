""" Exercício Python 061: Refaça o DESAFIO 051,
lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da
progressão usando a estrutura while. """
from time import sleep
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

sleep(1)
print('\033[1;92m-=-\033[m' * 15,
      '\n\033[97m               Gerador de PA'
      )
print('\033[1;92m-=-\033[m' * 15, '\n\033[97m')
sleep(0.5)

primeiro = int(input(' Primeiro termo: '))  # começar por qual número
razao = int(input(' Razão: '))  # pulando de 2 em 2, 3 em 3, 4 em 4, etc..

termo = primeiro
cont = 1

while cont <= 10:
    print(f' {termo} → ', end='')
    sleep(0.4)
    termo += razao
    cont += 1

print('\033[1;92m-=-\033[m' * 15,
      '\n\033[97m               Fim do programa'
      )
print('\033[1;92m-=-\033[m' * 15, '\n\033[97m')
# --------------------------------------------------------------------------



sleep(1)
print('\033[1;31m-=\033[m' * 11)
print('\033[1;34m Gerador de PA.\033[m')
print('\033[1;31m-=\033[m' * 11)
sleep(0.5)
primeiro = int(input('Primeiro termo: '))  # começar por qual número
razao = int(input('Razão: '))  # pulando de 2 em 2, 3 em 3, 4 em 4, etc..
termo = primeiro
cont = 1
while cont <= 10:
    print(f'\033[31m{termo} → ', end='\033[m')
    sleep(0.4)
    termo += razao
    cont += 1
print('\nFim')
