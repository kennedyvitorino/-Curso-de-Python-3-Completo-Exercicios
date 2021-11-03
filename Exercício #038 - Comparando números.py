"""Escreva um programa que leia dois números inteiros e comprare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

numero1 = int(input('Digite o 1º número:... '))
numero2 = int(input('Digite o 2º número:... '))

if numero1 > numero2:
    print(f'O número {numero1} é maior que o número {numero2}')

elif numero2 > numero1:
    print(f'O número {numero2} é maior que o número {numero1}')

else:
    print(f'Neste caso não existe maior nem menor. \n'
          f'O número {numero1} é igual ao número {numero2}')

# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 15,
      '\n\033[97m             Comparando números'
      )
print('\033[1;94m-=-\033[m' * 15)


num1 = int(input('\033[97m Primeiro número:.... '))
num2 = int(input(' Segundo número:..... '))

if num1 > num2:
    print(f'\n O número {num1} é maior que o {num2}\n')

elif num2 > num1:
    print(f'\n O número {num2} é maior que o {num1}zn')

else:
    print(f' Os dois valores são exatamente iguais.\n')

print('\033[1;94m-=-\033[m' * 15,
      '\n\033[97m             Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 15)

# --------------------------------------------------------------------------


numb1 = int(input('Informe o 1º número: '))
numb2 = int(input('Informe o 2º número: '))
if numb1 > numb2:
    print(f'O \033[1;37mprimeiro\033[m número é maior!')
elif numb2 > numb1:
    print(f'O segundo número é maior!')
else:
    print('Os \033[1;35mdois\033[m valores são exatamente iguais.')

# --------------------------------------------------------------------------


# cor = {'limpa':'\033[m',
#        'ver_negrito':'\033[1;31m',
#        'verm':'033[31m',
#        'verde':'\033[32m',
#        'verde_negrito':'\033[1;32m',
#        'pretoebranco':'\033[7;30m',
#        'azul':'\033[34m',
#        'azul_negrito':'\033[1;34m',
#        'negrito':'\033[1m'
#        }
# n1 = int(input(f'{cor["ver_negrito"]}Primeiro número: {cor["limpa"]}'))
# n2 = int(input(f'{cor["verde_negrito"]}Segundo número: {cor["limpa"]}'))
# if n1 > n2:
#     print(f'{cor["ver_negrito"]}O primeiro número é maior!{cor["limpa"]}')
# elif n2 > n1:
#     print(f'{cor["verde_negrito"]}O segundo número é maior!{cor["limpa"]}')
# else:
#     print(f'Os {cor["azul_negrito"]}dois{cor["limpa"]} valores são iguais.')

# --------------------------------------------------------------------------

# numero1 = int(input('[\033[1;33m1º\033[m] número: '))
# numero2 = int(input('[\033[1;34m2º\033[m] número: '))
# if numero1 > numero2:
#     print('\nO\033[1;33m1º\033[m número é maior!')
# elif numero2 > numero1:
#     print('\nO \033[1;34m2º\033[m número é maior!')
# else:
#     print('\nO \033[1;32mdois\033[m valores são \033[1;4miguais.')

