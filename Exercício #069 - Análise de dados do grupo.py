"""Exercício Python 069: Crie um programa que
leia a idade e o sexo de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""
from time import sleep
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
      '\n║\033[97m     Análise de dados do grupo\033[91m      ║ \n'
      '╚════════════════════════════════════╝\n\033[m\033[97m')

total18 = totalhomens = totalmulhermenor20 = totalmulher = 0

while True:
    idade = int(input(' Informe a sua idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input(' Qual é o seu sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        total18 += 1

    if sexo == 'M':
        totalhomens += 1

    if sexo == 'F' and idade < 20:
        totalmulhermenor20 += 1

    if sexo == 'F':
        totalmulher += 1

    resposta = ' '

    while resposta not in 'SN':
        resposta = str(input('\n Deseja continuar com o programa? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'\n Temos {total18} pessoas com mais de 18 anos cadastradas.\n'
      f'\n \033[91mTotalizando', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='\033[m')
sleep(0.5)
print(f'\n\n\033[97m {totalhomens} homens cadastrados.\n'
      f' {totalmulher} mulheres cadastadas.')
sleep(0.5)
print(f' E temos atualmente {totalmulhermenor20} moças com menos de 20 anos.')
sleep(0.5)
print()
print('\033[91m╔════════════════════════════════════╗'
      '\n║\033[97m          Fim do programa\033[91m           ║ \n'
      '╚════════════════════════════════════╝\n\033[m\033[97m')
# --------------------------------------------------------------------------


# tot_18 = tot_homens = tot_mulher_20 = 0
#
# while True:
#     idade = int(input('Informe a sua idade: '))
#     sexo = ' '
#     while sexo not in 'MF':
#         sexo = str(input('Qual é o seu sexo: [M/F] ')).strip().upper()[0]
#     if idade >= 18:
#         tot_18 += 1
#     if sexo == 'M':
#         tot_homens += 1
#     if sexo == 'F':
#         tot_mulher_20 += 1
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Deseja continuar com o programa? [S/N]')).strip().upper()[0]
#     if resp == 'N':
#         break
# print(f'Temos {tot_18} pessoas maiores de idade.')
# print(f'Totalizando', end='')
# sleep(0.5)
# print('.', end='')
# sleep(0.5)
# print('.', end='')
# sleep(0.5)
# print('.', end='')
# sleep(0.5)
# print(f' {tot_homens} homens cadastrados')
# sleep(0.5)
# print(f'E temos atualmente {tot_mulher_20} moças com menos de 20 anos.')
# sleep(0.5)
# print('End')

# tot18 = toth = totm20 = 0
# while True:
#     idade = int(input('Idade: '))
#     sexo = ' '
#     while sexo not in 'MF':
#         sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
#     if idade >= 18:
#         tot18 += 1
#     if sexo == 'M':
#         toth += 1
#     if sexo == 'F':
#         totm20 += 1
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
#     if resp == 'N':
#         break
# print(f'Total de pessoas com mais de 18 anos: {tot18}')
# print(f'Ao todo temos {toth} homens cadastrados.')
# print(f'E temos {totm20} mulheres com menos de 20 anos.')
