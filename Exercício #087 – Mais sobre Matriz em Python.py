""" Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

s_par = s_impar = maior = s_col_0 = s_col_1 = s_col_2= 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe um valor para [{l}, {c}]: '))

print('\033[91m+=\033[m' * 25)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:  # se for par
            s_par += matriz[l][c]
        else:
            s_impar += matriz[l][c]
    print()

print('\033[91m+=\033[m' * 25)
print(f'A soma dos valores pares é {s_par}\n'
      f'A soma dos valores ímpares é {s_impar}')
print('\033[91m+=\033[m' * 25)


for l in range(0, 3):
    s_col_0 += matriz[l][0]
print(f'A soma dos valores da primeira coluna são: {s_col_0}')

for l in range(0, 3):
    s_col_1 += matriz[l][1]
print(f'A soma dos valores da segunda coluna são: {s_col_1}')

for l in range(0, 3):
    s_col_2 += matriz[l][2]
print(f'A soma dos valores da terceira coluna são: {s_col_2}')
print('\033[91m+=\033[m' * 25)


for c in range(0, 3):

    if c == 0 or matriz[0][c] > maior:
        maior = matriz[0][c]
print(f'O maior elemento da primeira linha é: {maior}')

for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'O maior elemento da segunda linha é: {maior}')

for c in range(0, 3):
    if c == 0 or matriz[2][c] > maior:
        maior = matriz[2][c]

print(f'O maior elemento da terceira linha é: {maior}\n\n'
      f'{"Fim do programa":^50}')
