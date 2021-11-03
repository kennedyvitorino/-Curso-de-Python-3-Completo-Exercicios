"""Refaça o DESAFIO 9,mostrando a tabuada
de um número que o usuário escolher,
só que agora utilizando um laço for. """
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
from time import sleep

# contadores
s_par = cont_par = s_impar = cont_impar = 0

for cont in range(0, 7):
    num = int(input(f'Informe o {cont + 1}º inteiro: '))

    if num % 2 == 0:  # se for par
        s_par += num
        cont_par += 1

    elif num % 2 == 1:  # se for impar
        s_impar += num
        cont_impar += 1

print(f'Voce inseriu {cont_par} números pares. E a soma deles é {s_par} \n'
      f'Você inseriu {cont_impar} números ímpares. E a soma dele é {s_impar}')

# --------------------------------------------------------------------------


def titulo(msg):
    tamanho = len(msg) + 4
    print('\033[91m═\33[m' * tamanho)
    print(f'  {msg}')
    print('\033[91m═\33[m' * tamanho)
    sleep(0.25)


titulo('Tabuada versão 2.0')

numero = int(input('Digite um número para ver a sua tabuada: '))

print('\033[91m═\33[m' * 22)

for contador in range(1, 11):
    num = numero * contador
    print(f' {numero}x{contador} é igual a: {num}')
print('\033[91m═\33[m' * 22)

# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m                     Tabuada v2.0'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m', '')

num = int(input('   Digite um número para ver a sua tabuada: '))

for c in range(1, 11):
    print(f'   {num} x{c:2} é igual a {num * c}')
    sleep(0.20)

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m                   Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m')

# --------------------------------------------------------------------------

number = int(input('Informe um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'\n{number} x{c:2} é igual a: {number * c}\n')
    sleep(0.25)
print('\n')

# number1 = int(1)
# for c in range(1, 11):
#     print(f'{number1} x {c:2} é igual a: {number1 * c}')
# print('\n')
#
# number2 = int(2)
# for c in range(1, 11):
#     print(f'{number2}x {c:2} é igual a: {number2 * c}')
# print('\n')

# --------------------------------------------------------------------------p
