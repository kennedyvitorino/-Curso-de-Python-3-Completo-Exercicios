"""Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

temporaria = []
principal = []

maior = menor = 0

while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))

    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]

        if temporaria[1] < menor :
            menor = temporaria[1]

    principal.append(temporaria[:])
    temporaria.clear()

    resposta = str(input('Quer continuar? [S/N]'))

    if resposta in 'nN':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(principal)} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')

for pessoa in principal:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ', end='')

print()

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')

for pessoa in principal:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}] ', end='')

print()
