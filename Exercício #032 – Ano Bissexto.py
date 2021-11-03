"""Faça um program que leia um ano qualquer
e mostre se ele é BISSEXTO. Chama-se ano bissexto
o ano ao qual é acrescentado um dia extra, ficando
com 366 dias, um dia a mais do que os anos normais
de 365 dias, ocorrendo a cada quatro anos
(exceto anos múltiplos de 100 que não são múltiplos de 400)"""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------
from datetime import date

ano = int(input('Informe qual ano voce deseja validar se é BISSEXTO. \n'
                'Digite > 0 < para verificar o ano atual.'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO!')
else:
    print(f'O ano de {ano} não é BISSEXTO')

# --------------------------------------------------------------------------

year = int(input(f'Que ano você quer analisar?\n'
                 f'Digite 0 para analisar o ano atual:'))


if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano de {year} é bissexto!')
else:
    print(f'O ano de {year} não é bissexto!')


# --------------------------------------------------------------------------
print('\n\033[1;94m╔════════════════\033[m \033[1;97mANO BISSEXTO\033[m \033[1;94m════════════════╗\033[m\n')

year = int(input(f'      Que ano você quer analisar?\n'
                 f'      Digite 0 para analisar o ano atual:'))

if year == 0:
    year = date.today().year  # pega o ano atual que estiver configurado na maquina.

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'\n      O ano de {year} é bissexto!')

else:
    print(f'\n      O ano de {year} não é bissexto!')

print('\n\033[1;94m╚══════════════\033[m \033[1;97mFIM DO PROGRAMA\033[m \033[1;94m═══════════════╝\033[m')

# --------------------------------------------------------------------------


ano = int(input('\033[1;31mQue você ano quer analisar?\nColoque \033[m\033[m\033[1m0\033[1;31m para analisar o ano atual: \033[m'))
if ano == 0:
    ano = date.today().year  # pega o ano atual configurado na maquina.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;32mO ano de\033[m\033[1m{ano}\033[1;32m é BISSEXTO!\033[m')
else:
    print(f'\033[1;32mO ano de \033[m\033[1;35;4m{ano}\033[m\033[1;32m não é BISSEXTO!\033[m')

# --------------------------------------------------------------------------
print('\n\033[1;94m╔════════════════\033[m \033[1;97mANO BISSEXTO\033[m \033[1;94m════════════════╗\033[m\n')

year = int(input(f'      Que ano você quer analisar?\n'
                 f'      Digite 0 para analisar o ano atual:'))

if year == 0:
    year = date.today().year  # pega o ano atual que estiver configurado na maquina.

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'\n      O ano de {year} é bissexto!')

else:
    print(f'\n      O ano de {year} não é bissexto!')

print('\n\033[1;94m╚══════════════\033[m \033[1;97mFIM DO PROGRAMA\033[m \033[1;94m═══════════════╝\033[m')

# --------------------------------------------------------------------------

ano = int(input('\033[1;31mQue você ano quer analisar?\nColoque \033[m\033[m\033[1m0\033[1;31m para analisar o ano atual: \033[m'))
if ano == 0:
    ano = date.today().year  # pega o ano atual configurado na maquina.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;32mO ano de\033[m\033[1m{ano}\033[1;32m é BISSEXTO!\033[m')
else:
    print(f'\033[1;32mO ano de \033[m\033[1;35;4m{ano}\033[m\033[1;32m não é BISSEXTO!\033[m')

# --------------------------------------------------------------------------
# Regras para calcular o Ano Bissexto
# Para saber quando será Ano Bissexto devemos seguir o
# seguinte princípio: todos os anos múltiplos de 4 que
# também não são múltiplos de 100, com exceção dos múltiplos
# de 400, deverão ser anos bissextos.
# Por exemplo, 2004 e 2008 são múltiplos de 4 e, por este motivo,
# considerados anos bissextos. No entanto, 1900 e 1700 não foram
# anos bissextos, pois eram múltiplos de 100. Já o ano 2000, por
# outro lado, como é um múltiplo de 400, foi considerado ano bissexto.
