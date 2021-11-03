""" Exercício Python 064: Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag). """
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# Alt + 186 ║
# --------------------------------------------------------------------------

print('\033[92m╔════════════════════════════════════╗'
      '\n║\033[97m      Tratando vários números\033[92m       ║ \n'            
      '╚════════════════════════════════════╝\n\033[m\033[97m')

numero = contador = soma = 0

numero = int(input(' Digite um número: [9999 para encerrar]. '))

while numero != 9999:
    soma += numero
    contador += 1

    numero = int(input(' Digite um número: [9999 para encerrar]. '))

print(f'\n Você digitou {contador} e a soma entre eles é de {soma}')

# --------------------------------------------------------------------------


# print('\033[1;31m░▓▒\033[m' * 13)
# num = cont = soma = 0
# num = int(input('Informe um número: [999 para encerrar]'))  # 999 aqui assume a condição de parada.
# while num != 999:
#     soma += num
#     cont += 1
#     num = int(input('Informe um número: [999 para encerrar]'))  # 999 aqui assume a condição de parada.
# print(f'Você digitou {cont} números e a soma deles é {soma}')

num = 0  # ou num = cont = soma = 0
cont = 0  # ou num = cont = soma = 0
soma = 0  # ou num = cont = soma = 0
num = int(input('Digite um número: [999 para encerrar].'))   # 999 aqui assume a condição de parada.
while num != 999:
    soma = soma + num  # ou soma += 1
    cont = cont + 1  # ou cont += 1
    num = int(input('Informe um número: [999 para encerrar]'))  # 999 aqui assume a condição de parada.
print(f'Você digitou {cont} e a soma entre ele é de {soma}')

# --------------------------------------------------------------------------
