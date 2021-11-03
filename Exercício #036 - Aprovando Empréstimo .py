"""Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será negado."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

print(f'\033[1;30;107m{" Programa MINHA CASA, MINHA DÍVIDA ":•^57}\033[m')

casa = float(input('Qual o valor da propriedade que o senhor deseja adquirir? '))
salario = float(input('Qual o salário atual do senhor? '))
anos = int(input('Em quantos anos o senhor deseja pagar? '))

meses = 12 * anos

parcela = casa / (anos * 12)  # divide o valor da casa pela quantidade de anos vezes 12 (quantidade de meses de 1 ano)
minimo = salario * 30 / 100

if parcela <= minimo:
    print(f'A parcela será de R${parcela:.2f} em {meses}x em {anos} ano(s) \n'
          f'Deu bom')

else:
    print(f'Infelizmente não será desta vez! \n'
          f'Deu ruim')

# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m                Aprovando empréstimo'
      )
print('\033[1;94m-=-\033[m' * 18)

casa = float(input('\033[97m Quanto custa a casa que você deseja adquirir? R$'))
salario = float(input(' Qual é o salário mensal do comprador? R$'))
anos = int(input(' Em quantos anos o comprador deseja pagar? '))

parcela = casa / (anos * 12)
minimo = salario * 30 / 100

print(f' Para pagar uma casa que custa {casa:.2f}R$ em {anos} anos.\n'
      f' A parcela será de {parcela:.2f}R$ mensais')

if parcela <= minimo:
    print(' O empréstimo poderá ser concedido!\n'
          ' Parabéns!')

else:
    print(' Infelizmente o empréstimo não poderá ser concedido!')

# --------------------------------------------------------------------------


# cor = {'limpa': '\033[m',
#        'ver_negrito': '\033[1;31m',
#        'verm': '\033[31m',
#        'verde': '\033[32m',
#        'pretoebranco': '\033[7;30m',
#        'negrito': '\033[1m'
#        }
# casa1 = float(input(f'{cor["negrito"]}Valor da casa: {cor["limpa"]}'))
# salario1 = float(input(f'{cor["verde"]}Salário do comprador:{cor["limpa"]}R$'))
# anos1 = int(input(f'Quantos {cor["ver_negrito"]}anos{cor["limpa"]} de financiamento? '))
# prestacao1 = casa1 / (anos1 * 12)
# minimo1 = salario1 * 30 / 100
# print(f'Para pagar uma casa de {cor["verde"]}{cor["negrito"]}{casa1:.2f}R${cor["limpa"]} em {cor["ver_negrito"]}{anos1}{cor["limpa"]} anos!\nA prestação será de {prestacao1:.2f}')
# if prestacao1 <= minimo1:
#     print('O empréstimo será concedido!')
# else:
#     print('O empréstimo não será concedido!')
