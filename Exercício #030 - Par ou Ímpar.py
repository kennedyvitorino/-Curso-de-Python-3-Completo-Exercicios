"""Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou ÍMPAR."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

numero = int(input('Digite um número para verificar se é PAR ou ÍMPAR: '))

if numero % 2 == 0:
    print(f'Você digitou {numero} e é PAR!')
else:
    print(f'Você digitou {numero} e é ÍMPAR!')

# --------------------------------------------------------------------------

print('\n  ╔═══════════════ Par ou Ímpar ═══════════════╗ \n')

number = int(input('        Me diga um número qualquer\n'
                   '        E eu lhe direi se é par ou ímpar: '))

result = number % 2
if result == 0:
    print(f'\n        O número digitado foi {number}, e é par')
else:
    print(f'\n        O número digitado foi {number}, e é ÍMPAR')

print('\n  ╩══════════════ Fim do programa ══════════════╩')

# --------------------------------------------------------------------------


numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print(f'O número {numero} é PAR.')
else:
    print(f'O número {numero } é ÍMPAR.')


# --------------------------------------------------------------------------
