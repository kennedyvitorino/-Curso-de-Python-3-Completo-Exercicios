""" Exercício Python 063: Escreva um programa que leia um
número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8 """
from time import sleep
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
      '\n║\033[97m      Sequência de Fibonacci \033[92m       ║ \n'            
      '╚════════════════════════════════════╝\n\033[m\033[97m')

numero = int(input(' Termos a serem mostrados: '))

termo1 = 0
termo2 = 1

print(f' {termo1} → {termo2}', end='')

contador = 3  # aqui o contador recebe o valor 3 pq ja sabemos o 1º e o 2º termo

while contador <= numero:
    sleep(0.5)
    termo3 = termo1 + termo2
    print(f' → {termo3}', end='')

    termo1 = termo2
    termo2 = termo3
    print(f' → {termo3}', end='')

    contador += 1

print(f'\n Foram mostrados {contador} termos.')

print('\n\033[92m╔════════════════════════════════════╗'
      '\n║\033[97m          Fim do programa \033[92m          ║ \n'            
      '╚════════════════════════════════════╝\n\033[m\033[97m')

# --------------------------------------------------------------------------


print('\033[1;32m+_\033[m' * 11)
print('\033[1mSequência de Fibonacci\033[m')
print('\033[1;32m+-\033[m' * 11)
n = int(input('Termos a serem mostrados: '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')
cont = 3  # aqui o contador recebe o valor 3 pq ja sabemos o 1º e o 2º termo
while cont <= n:
    sleep(0.5)
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    print(f' → {t3}', end='')
    cont += 1
print('\n\nEnd')
