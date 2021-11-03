"""Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
viagens de até 200Km e R$0,45 para viagens acima de 200Km."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

distancia = float(input('Quantos KM terá a sua viagem? '))

if distancia <= 200:
    valor = distancia * 0.50
    print(f'Sua viagem foi de {distancia:.2f}Km \n'
          f'O preço a ser cobrado é de R${valor:.2f}')
else:
    valor = distancia * 0.45
    print(f'Sua viagem foi de {distancia:.2f}Km \n'
          f'O preço a ser cobrado é de R${valor:.2f}')

# --------------------------------------------------------------------------

dis = float(input('Quantos KM terá a sua viagem? '))

price = dis * 0.50 if dis <= 200 else dis * 0.45

print(f'A sua viagem foi de {dis:.2f}Km \n'
      f'E o preço a ser pago é R${price:.2f}')

# --------------------------------------------------------------------------

print('\n #---------- Calculando o custo da viagem ----------#\n')

distan = float(input('    Qual é a distância da sua viagem? '))

print(f'    Você está prestes a começar uma viagem de {distan}Km.')

if distan <= 200:
    valor = distan * 0.50

    print(f'    O preço da sua passagem será {valor:.2f}R$\n\n'
          f'    Boa viagem!')
else:
    valor = distan * 0.45

    print(f'    O preço da sua passagem será R${valor:.2f}R$\n\n'
          f'    Boa viagem!')

# --------------------------------------------------------------------------

dist = float(input('    Qual é a distânciada sua viagem? '))

print(f'    Você está prestes a começar uma viagem de {dist}Km.')

price1 = dist * 0.50 if dist <= 200 else dist * 0.45

print(f'    E o preço da sua passagem será de {price1:.2f}R$\n\n'
      f'    Faça uma boa viagem!')

# --------------------------------------------------------------------------

distancia = float(input('Qual é a distancia de sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}Km.\n')
if distancia <= 200:
    price = distancia * 0.50
    print(f'E o preço da sua passagem será de R${price}\n\n Boa viagem!')
else:
    price = distancia * 0.45
    print(f'E o preço da sua passagem será de R${price}\n\n Boa viagem!')