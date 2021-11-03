"""Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""
from random import randint
from time import sleep


compiuter = randint(0, 5)

humano = int(input('Digite um número: '))

if compiuter == humano:
    print(f'A maquina jogou {compiuter}, você acertou!')
else:
    print(f'A maquina jogou {compiuter}, você perdeu!')

# --------------------------------------------------------------------------

print('\n\033[1;94m═════════════\033[m \033[1;97mJogo da Adivinhação\033[m \033[1;94m═════════════\033[m')

# --------------------------------------------------------------------------
#  alt + 219 █
# alt + 220 ▄


compiuter = randint(0, 5)  # faz o compiuter randomizar, ou seja, gerar um número aleatório de 0 a 5

print(f'\033[1;94m-=-\033[m' * 16, '\n'
      f'    Estou pensando em um número entre 0 e 5.\n'
      f'            Tente adivinhar, humano!\n',
      f'            \033[1;91m___MUAHAHAHAHAHAHA___\033[m\n',
      f'\033[1;94m-=-\033[m' * 16
      )

player1 = int(input('    Em que número eu pensei?'))
print('\n    PROCESSANDO ', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m', end='')
sleep(0.25)
print('\033[1;94m█\033[m')
sleep(1.2)
if player1 == compiuter:
    print('    O homem venceu a maquina!')
else:
    print('    A maquina venceu o homem!')

# --------------------------------------------------------------------------

# computer = randint(0, 5)  # Faz o computador "PENSAR".
# print('-=-' * 20, '\n  Vou pensar em um número entre 0 e 5. Tente adivinhar...')
# print('-=-' * 20)
# player = int(input('\nEm que número eu pensei?? '))  # O player (variável) tentar adivinhar.
# print('_' * 17, '\nPROCESSANDO. . . ')
# print('-' * 115)
# # sleep(1.5)
# if player == computer:
#     print('\nAcertou miseraviiii! kKKkkkkkkkk')
# else:
#     print('\nNão foi dessa vez... e nem será da proxima, vacilaumm! kkjkj')
