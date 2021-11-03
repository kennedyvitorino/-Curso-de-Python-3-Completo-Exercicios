"""Faça um mini-sistema que utilize o Interactive Help
do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra ‘FIM’,
o programa se encerrará. Importante: use cores."""
from time import sleep

c = ('\033[m',  # 0 - Sem cores
     '\033[0;30;41m',  # 1 - Vermelho
     '\033[0;30;42m',  # 2 - Verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[1;30;107m'  # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0])
    sleep(1.5)


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')

    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(c[0])
    sleep(1)


# Programa Pricipal
comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)

    comando = str(input('Função ou Biblioteca >>> '))

    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)
