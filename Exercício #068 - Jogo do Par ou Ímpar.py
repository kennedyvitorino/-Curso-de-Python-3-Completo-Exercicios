""" Exercício Python 068: Faça um programa que jogue
par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo."""
from random import randint
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# Alt + 186 ║
# --------------------------------------------------------------------------

print('\033[91m╔════════════════════════════════════╗'
      '\n║\033[97m        Jogo do PAR ou ÍMPAR\033[91m        ║ \n'
      '╚════════════════════════════════════╝\n\033[m\033[97m')
v = 0

while True:
    jogador = int(input(' Digite um valor: '))
    compiuter = randint(0, 11)
    total = jogador + compiuter
    tipo = ' '

    while tipo not in 'PpIi':
        tipo = str(input(' Par ou Ímpar? [P/I] ')).strip().upper()
    print(f' Você jogou {jogador} e o compiuter {compiuter}\n'
          f' Deu Par.' if total % 2 == 0 else ' Deu Ímpar.\n')

    if tipo == 'P':
        if total % 2 == 0:  # o total DIVIDIDO POR 2 DEU RESTO 0 é par.
            print(f' Você venceu, humano!')
            v += 1
        else:
            print(f' A maquina venceu você, humano.')
            break

    elif tipo == 'I':
        if total % 2 == 1:  # o total DIVIDIVO POR 2 DEU RESTO 1 é ímpar
            print(' Você venceu, humano!')
            v += 1
        else:
            print(f' A maquina venceu, humano!')
            break
    print(' Vamos jogar novamente!\n')
print(f' Game Over!\n'
      f' Você venceu {v} vezes.\n')
print('\033[91m╔════════════════════════════════════╗'
      '\n║\033[97m           Fim do programa\033[91m          ║ \n'
      '╚════════════════════════════════════╝\n\033[m\033[97m')

# --------------------------------------------------------------------------


v = 0
print('\033[1;31m═\033[m' * 22)
print(' Jogo do PAR ou IMPAR.')
print('\033[1;31m═\033[m' * 22)
while True:
    player = int(input('Diga um valor: '))
    compiuter = randint(0, 11)
    total = player + compiuter
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print(f'Você jogou {player} e o \033[1;32mCompiuter\033[m {compiuter} e total {total}')
    print('Deu Par.' if total % 2 == 0 else 'Deu Ímpar.')
    if tipo == 'P':
        if total % 2 == 0:  # o total DIVIDIDO POR 2 DEU RESTO 0 é par.
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:  # o total DIVIDIVO POR 2 DEU RESTO 1 é ímpar
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos Jogar Novamente.')
print(f'\033[1;46mGame Over!\033[m Você venceu {v} vezes')
