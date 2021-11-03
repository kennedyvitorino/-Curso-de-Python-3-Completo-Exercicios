""" Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador
vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer. """
from time import sleep
from random import randint
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m             Jogo da Adivinhação v2.0'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

compiuter = randint(0, 10)

print(' Olá, eu sou a IA (mal paga, rs) do seu COMPIUTER', end='')
sleep(0.7)
print('\033[1;31m.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.\033[m', end='')
sleep(1)
print('\n\n\033[m \033[97mAcabei de pensar em num número entre 0 e 10.')
sleep(1)
print('\n Será que você pode adivinhar qual foi?')
sleep(1)
print('\n\033[1;91m             AAAHA HAAHAHAHAHAHAHHA...\033[m\n')
sleep(1)
acertou = False
palpites = 0

while not acertou:
    player = int(input('\033[97m Qual é o seu palpite: '))
    palpites += 1  # + = a 1, ou seja, mais um palpite

    if player == compiuter:
        acertou = True

    else:
        if player < compiuter:
            sleep(0.8)
            print(' Mais...')
            sleep(0.8)
            print('\n Tente mais uma vez!')

        elif player > compiuter:
            sleep(0.8)
            print(' Menos...')
            sleep(0.8)
            print('\n Tente mais uma vez!')

print(f'\n Humano(a), você acertou depois de {palpites} tentativas!\n')
sleep(1)
print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m             Fim do programa'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')
# --------------------------------------------------------------------------


computer = randint(0, 10)
print('Olá, sou a IA do seu COMPIUTER', end='')
sleep(0.5)
print('\033[1;31m.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.\033[m', end='')
sleep(1)
print('\n\n\033[97mAcabei de pensar em um número entre 0 e 10.')
sleep(1)
print('\nSerá que você consegue adivinhar qual foi?')
sleep(1)
print('\n\033[31mAAAH AHAHHAHAHAHAHA...\033[m')
sleep(1)
acertou = False
palpites = 0
while not acertou:
    player = int(input('Qual é o seu palpite? '))
    palpites += 1  # + = a 1, ou seja, mais um palpite
    if player == computer:
        acertou = True
    else:
        if player < computer:
            sleep(0.5)
            print('Mais...')
            sleep(0.5)
            print('Tente mais uma vez.')
        elif player > computer:
            sleep(0.5)
            print('Menos...')
            sleep(0.5)
            print('Tente mais uma vez.')
            sleep(0.5)
print(f'Acertou depois de {palpites} tentativas!')
