"""Crie um ALGORITMO que leia o preço de um PRODUTO
e mostre o seu novo PREÇO com 5% de desconto"""

valor = float(input('Digite um valor para que seja aplicado o desconto de 5%: '))

desconto = (valor * 5) / 100
valor_final = valor - desconto

print(f'R${valor:.2f} menos R${desconto:.2f} (5%) é igual a R${valor_final:.2f}')

# --------------------------------------------------------------------------

print('        *========== CALCULANDO DESCONTOS ==========*\n\n')

valor = float(input('Informe o valor do produto para receber os 5% de desconto: R$'))

desconto = (valor * 5) / 100
reais = valor - desconto

print(f'\nO valor inicial do produto era {valor:.2f}R$, e com o desconto de {desconto:.2f}R$ ficou no total de {reais:.2f}R$')

# --------------------------------------------------------------------------
