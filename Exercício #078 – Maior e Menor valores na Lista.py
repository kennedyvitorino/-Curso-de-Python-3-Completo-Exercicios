"""Exercício Python 078: Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista."""
# ----------------------------------------------------

lista_numerica = list()

maior = 0  # contador
menor = 0  # contador

for contador in range(0, 5):
    lista_numerica.append(int(input(f'Para a posição \033[1;91m{contador}\033[m, insira um valor:... ')))
    if contador == 0:
        maior = menor = lista_numerica[contador]
    else:
        if lista_numerica[contador] > maior:
            maior = lista_numerica[contador]

        if lista_numerica[contador] < menor:
            menor = lista_numerica[contador]

# print('\033[92m▀\033[m' * 27)
# print(f'Foram digitados os valores {lista_numerica} ')
#
# print(f'O maior valor digitado foi {maior} nas posições ', end='')
# for indice, valor in enumerate(lista_numerica):
#     if valor == maior:
#         print(f'{indice}... ', end='')
#
# print(f'\nO menor valor foi {menor} nas posições ', end='')
# for indice, valor in enumerate(lista_numerica):
#     if valor == menor:
#         print(f'{indice}... ', end='')

print(maior, menor)