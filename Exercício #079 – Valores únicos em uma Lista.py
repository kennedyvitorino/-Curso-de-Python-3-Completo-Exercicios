"""Exercício Python 079: Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro,ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente."""
# ----------------------------------------------------

# lista_N = list()
#
# while True:
#     numeros = int(input('Digite um valor: '))
#     if numeros not in lista_N:
#         lista_N.append(numeros)
#     else:
#         print('Valor duplicado! Não será adicionado!')
#
#     resposta = str(input('Quer continuar? [S/N]')).strip().lower()
#     if resposta in 'Nn':
#         break
#
# print('▀' * 28)
# lista_N.sort()
# print(f'Você digitou os valores {lista_N} \n'
#       f'\nFim do programa')

# ----------------------------------------------------

ListaN = list()

while True:
    num = int(input('Informe um valor: '))
    if num not in ListaN:
        ListaN.append(num)
    else:
        print('Este valor já foi adicionado! Por favor insira um valor diferente!')

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuar in 'Nn':
        break

print('▀' * 25)
ListaN.sort()
print(f'Foram adicionados os valores {ListaN} na nossa lista.\n\n'
      f'Fim do programa')