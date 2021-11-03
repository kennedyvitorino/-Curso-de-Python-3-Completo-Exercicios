"""Crie um programa onde o usuário possa digitar sete
valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente."""

lista_numeros = [[], []]

valor = 0

for contador in range(1, 8):
    valor = int(input('Informe um valor: '))
    if valor % 2 == 0:
        lista_numeros[0].append(valor)
    else:
        lista_numeros[1].append(valor)

print('+' * 30)

lista_numeros[0].sort(), lista_numeros[1].sort()  # .sort para deixar em ordem crescente

print(f'Todos os valores digitados foram: {lista_numeros}\n'
      f'Todos os valores pares digitados foram: {lista_numeros[0]}\n'
      f'Todos os valores ímpares digitados foram: {lista_numeros[1]}\n\n'
      f'Fim do programa')
