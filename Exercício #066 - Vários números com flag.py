""" Exercício Python 066: Crie um programa que leia números
inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi
a soma entre elas (desconsiderando o flag). """
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# Alt + 186 ║
# --------------------------------------------------------------------------

print('\033[96m╔════════════════════════════════════╗'
      '\n║\033[97m      Vários números com flag\033[96m       ║\n'            
      '╚════════════════════════════════════╝\n\033[m\033[97m')

numero = contador = soma = 0
numero = int(input(' Número: '))

while True:
    numero = int(input(' Número: '))
    if numero == 9999:
        break
    soma += numero
    contador += 1

print(f' Você digitou {contador} números e a soma entre eles é {soma}.')

print('\033[96m╔════════════════════════════════════╗'
      '\n║\033[97m          Fim do programa\033[96m           ║\n'            
      '╚════════════════════════════════════╝\n\033[m\033[97m')

# --------------------------------------------------------------------------


# num = cont = soma = 0
# num = int(input('Número: '))
# while True:
#     num = int(input('Número: '))
#     if num == 999:
#         break
#     soma += num
#     cont += 1
# print(f'Você digitou {cont} e a soma entre eles é {soma}')

# soma = cont = 0
# while True:
#     print('\033[1;32m*-\033[m' * 9)
#     n = int(input('Digite um número: '))
#     if n == 999:
#         break
#     soma += n
#     cont += 1
#
# print(f'Foram digitados {cont} números, e a soma deles é {soma}')

# --------------------------------------------------------------------------


soma = cont = 0
while True:
    print('\033[1;31m=◙=\033[m' * 6)
    n = int(input('\033[1mInforme um número: \033[m'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Números digitados: {cont}\nSoma: {soma}')
