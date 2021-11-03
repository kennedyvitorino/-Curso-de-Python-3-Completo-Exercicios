"""Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
-1 para bínário
-2 para octal
-3 para hexadecimal"""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

print(f"\033[1;30;100m{' Conversão de Bases Numéricas ':•^44}\033[m")

numero = int(input('\nDigite um número inteiro:'))

print("""Agora escolha uma das bases numéricas abaixo para conversão: 
[1] Binário
[2] Octal
[3] hexadecimal""")

option = int(input('Qual é a sua escolha: '))

if option == 1:
    print(f'\n{numero} convertido para BINÁRIO é igual a {bin(numero)} ou {bin(numero)[2:]}')

elif option == 2:
    print(f'\n{numero} convertido para OCTAL é igual a {oct(numero)} ou {oct(numero)[2:]}')

elif option == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)} ou {hex(numero)[2:]}')

else:
    print('Opção inválida, tente novamente!')