""" Exercício Python 53: Crie um programa que leia uma frase
qualquer e diga se ela é um palíndromo, desconsiderando os
espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA,
A TORRE DA DERROTA,
O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA. """
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m              Detectando Palíndromos'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

frase = str(input(' Digite uma frase qualquer: ')).strip().upper()

palavras = frase.split()
juntar = ''.join(palavras)
str_inversa = juntar[:: - 1]

print(f'\n O inverso de {juntar}\n'
      f' é {str_inversa}\n')

if str_inversa == juntar:
    print(' Temos um palíndromo!\n')

else:
    print(' Não temos um palíndromo!\n')

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m                   Fim do programa'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

# --------------------------------------------------------------------------

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m              Detectando Palíndromos'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

frasE = str(input(' Digite uma frase qualquer: ')).strip().upper()  # .strip() retirar espaços antes e depois.

palavras = frasE.split()  # .strip() para jogar o valores em uma lista.
juntar = ''.join(palavras)
inverso = ''

for letra in range(len(juntar) -1, -1, -1):  # mostrar a última letra da string e voltar de 1 em 1.
    inverso += juntar[letra]

print(f'\n O inverso de {juntar} é {inverso}')

if inverso == juntar:
    print(' Temos um palíndromo!\n')

else:
    print(' Não temos um palíndromo!\n')

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m                   Fim do programa'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

# --------------------------------------------------------------------------
# frase = str(input('Digite uma frase: ')).strip().upper()  # .strip() retirar espaços antes e depois.
# palavras = frase.split()  # .strip() para jogar o valores em uma lista.
# juntar = ''.join(palavras)
# string_inversa = ''
# for letra in range(len(juntar) - 1, -1, -1):
#     string_inversa += juntar[letra]
# print(f'\nO inverso de {juntar} é {string_inversa}')
# if string_inversa == juntar:
#     print('\nTemos um Palíndromo!')
# else:
#     print('\nNão temo um palíndromo!')
