"""Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento."""

print('-=' * 10)
print('  Aumento Salarial')
print('-=' * 10)

salario = float(input('Salário atual: R$'))

reajuste = (salario * 15) / 100
novo_salario = salario + reajuste

print(f'O salário antigo era R${salario:.2f} \n'
      f'Com o novo reajuste de R${reajuste:.2f} (15%), passará a ser R${novo_salario:.2f}  \n'
      f'Fim do programa.')

# --------------------------------------------------------------------------

print('\n╬╬╬╬╬╬╬╬╬╬ CALCULANDO AUMENTO NO SALÁRIO ╬╬╬╬╬╬╬╬╬╬\n')

salario = float(input('Quanto você recebe?'))

novo_salario = salario + (salario * 15 / 100)  # fórmula para calcular os 15% de aumento do salário

print(f'\nO seu salário era {salario:.2f}R$ e com 15% de aumento passou a ser {novo_salario:.2f}R$')

# --------------------------------------------------------------------------

sa = float(input('•Informe o salário do funcinário? R$ '))

# pra calcular o acréscimo de 15% no salário do funcionário
# é necessário multiplicar o salário por 15 e dividir por 100
# e depois somar o salário com salário
nsa = sa + (sa * 15 / 100)

print(f'\n •Um funcionário que antes recebia {sa:.2f}R$, agora com 15% de aumento passa a receber {nsa:.2f}R$\n\n    •Fim do exercício. Continue assim!')

# --------------------------------------------------------------------------

# Exercíciio extra:
# Faça um programa que leia o valor atual de um produto
# e qual seu preço final com desconto de 21% avista, e parcelado com 8% juros

produto = float(input('Qual é o preço do produto? R$'))

desconto = produto - (produto * 8 / 100)
acrescimo = produto + (produto * 21 / 100)

print(f'O produto que você escolheu, no pagamento avista fica no valor de {desconto:.2f}R$.\n'
      f'Se for parcelado terá o acréscimo de 8% totalizando {acrescimo:.2f}R$.')

# --------------------------------------------------------------------------
