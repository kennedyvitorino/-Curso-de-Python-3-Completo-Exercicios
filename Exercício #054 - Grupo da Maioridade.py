""" Exercício Python 54: Crie um programa que leia o ano de nascimento
 de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
 a maioridade e quantas já são maiores. """
from datetime import date
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m                Grupo da maioridade'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

ano_atual = date.today().year
tot_maior = 0
tot_menor = 0

for pessoa in range(1, 8):
    nascimento = int(input(' Em que ano a pessoa nasceu? '))
    idade = ano_atual - nascimento

    if idade >= 21:
        tot_maior += 1

    else:
        tot_menor += 1

print(f'\n Ao todo tivemos {tot_maior} maiores de idade.\n'
      f' E {tot_menor} menores de idade.\n')

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m                   Fim do programa'
      )
print('\033[1;92m-=-\033[m' * 18)

# --------------------------------------------------------------------------


# nasci = int(input('Em que ano a pessoa nasceu? '))
# atual = date.today().year
# totalmaior = 0
# totalmenor = 0
# for pesso in range(1, 8):
#     nasci = int(input('Em que ano a pessoa nasceu? '))
#     idade = atual - nasci
#     if idade >= 21:
#         totalmaior += 1
#         print('Essa pessoa é maior')
#     else:
#         totalmenor += 1
#         print('essa pessoa é menor')
# print(f'Ao todo tivemos {totalmaior} maiores.')
# print(f'E {totalmenor} menores.')

# --------------------------------------------------------------------------


# primeira parte: descobrindo a idade do usuário.
# nasci = int(input('Em que ano a pessoa nasceu? '))
# atual = date.today().year
# idade = atual - nasci
# if idade >= 21:
#     print('Essa pessoa é maior.')
# else:
#     print('Essa pessoa é menor.')

# --------------------------------------------------------------------------


# atual = date.today().year
# totmaior = 0
# totmenor = 0
# for people in range(1, 8):
#     birth = int(input(f'Em que ano a {people}ª pessoa nasceu? '))
#     age = atual - birth
#     if age >= 21:
#         totmaior += 1
#     else:
#         totmenor += 1
# print(f'Ao todos tivemos {totmaior} pessoas maiores de idade.')
# print(f'E também tivemos {totmenor} pessoas menores de idade.')

# --------------------------------------------------------------------------
