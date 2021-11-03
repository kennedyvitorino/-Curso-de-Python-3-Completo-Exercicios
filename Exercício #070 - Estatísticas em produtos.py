""" Exercício Python 070: Crie um programa que leia o nome
e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.  """
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# Alt + 186 ║
# --------------------------------------------------------------------------

print('\033[94m╔════════════════════════════════════╗'
      '\n║\033[97m     Estastísticas de produtos\033[94m      ║ \n'
      '╚════════════════════════════════════╝\n\033[m\033[97m')

total = totalMIL = contador = menor = 0
barato = ' '

while True:
    produto = str(input(' Nome do produto: '))
    preco = float(input(' Preço do produto: '))
    contador += 1
    total += preco

    if preco > 1000:
        totalMIL += 1

    if contador == 1 or preco < menor:
        menor = preco
        barato = produto

    resposta = ' '

    while resposta not in 'SN':
        resposta = str(input(' Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print(f' O total da compra foi de {total:.2f}R$\n'
      f' Temos {totalMIL} produtos custando mais de 1000.00R$.\n'
      f' O produto mais barato foi {barato} que custa {menor:.2f}R$')
print('\033[94m╔════════════════════════════════════╗'
      '\n║\033[97m          Fim do programa\033[94m           ║ \n'
      '╚════════════════════════════════════╝\n\033[m\033[97m')


# --------------------------------------------------------------------------


total = total_1000 = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        total_1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

fim = '\033[m Fim do programa.\033[1;31m '
print(f'O total da compra foi {total:.2f}R$')
print(f'Temos {total_1000} produtos custando mais de 1000.00R$.')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}R$')
print(f'\033[1;31m{fim:═^40}\033[m')
