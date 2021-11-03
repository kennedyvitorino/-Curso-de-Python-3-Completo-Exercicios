"""Crie um programa que vai ler vários números e
colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

# --------------------------------------------------------------------------


lista = []

while True:
    lista.append(int(input('Entre com um valor: ')))
    resposta = str(input('Deseja continuar? '))
    if resposta in 'Nn':
        break

print('-' * 35)
print(f'Foram digitados {len(lista)} elementos \n')

lista.sort(reverse=True)

print(f'A lista ordenada de forma decrescente é {lista}')

if 5 in lista:
    print('O valor faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')

print('Fim do programa!')
