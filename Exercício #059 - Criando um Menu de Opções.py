"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
from time import sleep
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m              Criando um menú de opções'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

num1 = int(input('\n Primeiro valor: '))
num2 = int(input(' Segundo valor: '))

opcao = 0

while opcao != 5:
    print("""\n [1] Somar
 [2] Multiplicar
 [3] Maior
 [4] Novos números
 [5] Sair do programa""")

    opcao = int(input('\n Qual é a sua opçao?'))
    if opcao == 1:
        soma = num1 + num2
        print(f' Somando {num1} com {num2} temos {soma}')

    elif opcao == 2:
        produto = num1 * num2
        print(f' Multiplicando {num1} com {num2} temos {produto}')

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m             Fim do programa'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

# --------------------------------------------------------------------------


n1 = int(input(' Primeiro valor:'))
n2 = int(input(' Segundo valor :'))
option = 0
while option != 5:
    print("""    [1]  somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa""")
    option = int(input('>>>>Qual é a sua opção? '))
    if option == 1:
        soma = n1 + n2
        print(f'Somando {n1} com {n2} temos {soma}')
    elif option == 2:
        prod = n1 * n2
        print(f'Multiplicando {n1} por {n2} temos {prod}')
