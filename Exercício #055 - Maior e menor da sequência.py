"""  Exercício Python 055: Faça um programa que leia
o peso de cinco pessoas. No final, mostre qual foi
o maior e o menor peso lidos."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;92m-=-\033[m' * 15,
      '\n\033[97m Verificando o maior e o menor da sequência'
      )
print('\033[1;92m-=-\033[m' * 15, '\n\033[97m')

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f' Qual é o peso da {p}ª '))

    if peso == 1:
        maior = peso
        menor = peso

    else:

        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print(f'\n O menor peso foi {menor}\n'
      f' O maior peso foi {maior}\n')

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m                  Fim do programa'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')
# --------------------------------------------------------------------------


# print('\033[1;31m-=\033[m' * 14)
# print('\033[1;37mMAIOR E MENOR DA SEQUENCIA.\033[m')
# print('\033[1;31m-=\033[m' * 14)
# maior = 0
# menor = 0
# for p in range(1, 6):
#     peso = float(input(f'Peso: '))
#     if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print(f'Maior peso: {maior}')
# print(f'Menor peso: {menor}')

# print('\033[1;31m-=\033[m' * 14)
# print('\033[1;37mMAIOR E MENOR DA SEQUENCIA.\033[m')
# print('\033[1;31m-=\033[m' * 14)
# maior = 0
# menor = 0
# for p in range(1, 6):
#     peso = float(input(f'Peso da {p}ª pessoa: '))
#     if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print(f'O maior peso é: {maior}')
# print(f'O menor peso é: {menor}')





















