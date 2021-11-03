"""Crie um programa que declare uma
matriz de dimensão 3×3 e preencha com valores
lidos pelo teclado. No final, mostre a matriz
na tela, com a formatação correta."""

matriz_lista = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

# estrutura de repetição para guardar valores na memoria
for linha in range(0, 3):
    for contador in range(0, 3):
        matriz_lista[linha][contador] = int(input(f'Digite um valor para {[linha], [contador]}: '))

print('+=' * 20)

# estrutura de repetição para mostrar o que foi guardado na memoria pela estrutura anterior
for linha in range(0, 3):
    for contador in range(0, 3):
        print(f' [{matriz_lista[linha][contador]:^5}]', end='')
    print()
print('\nFim do programa')
