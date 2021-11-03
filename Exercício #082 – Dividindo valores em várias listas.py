"""Crie um programa que vai ler vários números e
colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os
valores ímpares digitados, respectivamente. Ao final,
mostre o conteúdo das três listas geradas."""

# --------------------------------------------------------------------------

lista_num = list()    # vetor
lista_par = list()    # vetor
lista_impar = list()  # vetor

while True:
    lista_num.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar? [S/N]'))

    if resposta in 'nN':
        break

for indice, valor in enumerate(lista_num):
    if valor % 2 == 0:
        lista_par.append(valor)

    if valor % 2 == 1:
        lista_impar.append(valor)

print(f'A lista completa é {lista_num} \n'
      f'A lista de pares é {lista_par} \n'
      f'A lista de ímpares é {lista_impar} \n'
      f'Fim do programa')

# --------------------------------------------------------------------------

numeros_lista = list()
pares_lista = list()
impares_lista = list()

while True:
    numeros_lista.append(int(input('Insira um valor para ser adicionado a uma lista: ')))
    resposta = str(input('Você deseja continuar? [S/N]'))

    if resposta in 'Nn':
        break

for indice, valor in enumerate(numeros_lista):
    if valor % 2 == 0:
        pares_lista.append(valor)

    if valor % 2 == 1:
        impares_lista.append(valor)

print(f'A lista completa é {numeros_lista} \n'
      f'A lista de pares é {pares_lista} \n'
      f'A lista de ímpares é {impares_lista}')
