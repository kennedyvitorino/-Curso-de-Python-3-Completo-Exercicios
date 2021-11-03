"""Crie um programa que faça o computador jogar jokenpô com você!"""
from random import randint
from time import sleep
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m              Pedra Papel e Tesoura'
      )
print('\033[1;94m-=-\033[m' * 18, '\n')

item = ('Pedra', 'Papel', 'Tesoura')  # colocando as opções para jogar dentro de uma tupla.
compiuter = randint(0, 2)

play = int(input('''\033[97m  Suas opções:\n
  [0] Pedra
  [1] Papel
  [2] Tesoura\n
  Qual é a sua jogada? '''))

sleep(0.5)
print('\n\033[1;92m        JO', end='')
sleep(0.5)
print('KEN', end='')
sleep(0.5)
print('PÔ!!!\033[m')
sleep(0.5)

print('\n', '\033[1;31m=\033[m-' * 13)
print(f'  O compiuter jogou {item[compiuter]}')
print(f'  O jogador jogou {item[play]}')
print('', '\033[1;31m=\033[m-' * 13, '\n')

if compiuter == 0:  # compiuter jogou PEDRA.
    if play == 0:  # jogador tb jogou PEDRA.
        print('  Empatou!\n')

    elif play == 1:  # jogador jogou PAPEL.
        print('  O jogador venceu!\n')

    elif play == 2:  # jogador jogou TESOURA.
        print('  Perdeu, humano...\n'
              '  A maquina venceu!\n')

    else:
        print('  Jogada Inválida!\n')

elif compiuter == 1:  # o compiuter jogou PAPEL.
    if play == 0:  # jogador jogou PEDRA.
        print('  Perdeu, humano!\n'
              '  A maquina venceu!\n')

    elif play == 1:  # jogador jogou PAPEL.
        print('  Empatou!\n')

    elif play == 2:  # jogador jogou TESOURA.
        print('  O jogador venceu!\n')

    else:
        print('  Jogada Inválida!\n')

elif compiuter == 2:  # compiuter jogou TESOURA.
    if play == 0:  # jogador jogou PEDRA.
        print('  O jogador venceu!\n')

    elif play == 1:  # jogador jogou PAPEL.
        print('  Perdeu, humano!\n'
              '  A maquina venceu!\n')

    elif play == 2:  # jogador jogou TESOURA.
        print('  Empatou!\n')

    else:
        print(' Jogada Inváluda!\n')

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m                   Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 18, '\n')

# --------------------------------------------------------------------------

# itens = ('Pedra', 'Papel', 'Tesoura')
# computer = randint(0, 2)
# print('''Suas opções:
# [0] Pedra
# [1] Papel
# [2] Tesoura''')
# # print(f'O computador escolheu: {itens[computer]}')
# player = int(input('\nQual é a sua jogada? '))
# print(f'\033[1;31m=\033[m-' * 12)
# print(f'O computador jogou {itens[computer]}')
# print(f'O jogador jogou {itens[player]}')
# print(f'\033[1;31m=\033[m-' * 12)
# if computer == 0:  # computador jogou PEDRA.
#     if player == 0:  # jogador também jogou PEDRA.
#         print('Empate!')
#     elif player == 1:  # jogador jogou PAPEL.
#         print('Jogador vence!')
#     elif player == 2:  # jogador jogou TESOURA.
#         print('Perdeu, boy!\nA maquina lhe venceu!')
#     else:
#         print('Jogada Inválida!!!')
# elif computer == 1:  # computador jogou PAPEL.
#     if player == 0: # jogador jogou PEDRA.
#         print('Perdeu, boy!\nA maquina lhe venceu!')
#     elif player == 1: # jogador jogou PAPEL.
#         print('Empate!')
#     elif player == 2: # jogador jogou TESOURA.
#         print('Jogador vence!')
#     else:
#         print('Jogada Inválida!!!')
# elif computer == 2:  # computador jogou TESOURA.
#     if player == 0: # jogador jogou PEDRA.
#         print('Jogador vence!')
#     elif player == 1: # jogador jogou PAPEL.
#         print('Não foi dessa vez!\nA maquina venceu!')
#     elif player == 2: # jogador jogou TESOURA.
#         print('Empate!!!')
#     else:
#         print('Jogada Inválida!!!')
