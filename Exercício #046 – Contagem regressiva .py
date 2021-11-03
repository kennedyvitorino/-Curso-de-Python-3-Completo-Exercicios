"""Faça um programa que mostre na tela uma contagem
regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles """
from time import sleep
import emoji
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

print(f'   \033[1;30;101m{" Contagem regressiva para o estouro dos fogos ":•^56}\033[m')

for fogos in range(10, -1, -1):
    print(fogos, end=' ')
    sleep(0.5)

print('\n\033[1;30;101mBOOM BOOM POOW!\033[m')

# --------------------------------------------------------------------------


print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m             Contagem regressiva'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m')

for contador in range(10, -1, -1):
    print(contador, end=' → ')
    sleep(0.5)

print(emoji.emojize(f'\n\n\033[1;91m            BUM :fireworks: BUM :fireworks: POOW :fireworks:\033[m', use_aliases=True))

# --------------------------------------------------------------------------

# for c in range(0, 11):
for variavel_controle in range(10, -1, -1):
    print(variavel_controle)
    sleep(0.5)
print('\033[1;31mBUM! BUM! POOOW!\033[m')
