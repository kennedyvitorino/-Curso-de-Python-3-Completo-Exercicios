"""Faça um programa que leia três números
e mostre qual é o maior e qual é o menor."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

A = int(input('Digite o primeiro número: '))
B = int(input('Digite o segundo número: '))
C = int(input('Digite o terceiro número: '))

me = A

if B < C and B < A:
    me = B
if C < B and C < A:
    me = C

ma = A

if B > C and B > A:
    ma = B
if C > B and C > A:
    ma = C

print(f'O número maior foi {ma} \n'
      f'O número menor foi {me}')

# --------------------------------------------------------------------------

print('\n\033[1;94m╔════════\033[m \033[1;97mMAIOR E MENOR\033[m \033[1;94m════════╗\033[m\n')

a1 = int(input('       Primeiro número:... '))
b1 = int(input('       Segundo número:.... '))
c1 = int(input('       Terceiro número:... '))

# Verificando quem é o menor valor.
menor1 = a1  # aqui declaramos a variável a1 como o menor valor

if b1 < a1 and b1 < c1:
    menor1 = b1

if c1 < a1 and c1 < b1:
    menor1 = c1

#  verificando quem é o maior valor.
maior1 = a1  # aqui declaramos a variável a1 como o maior valor

if b1 > a1 and b1 > c1:
    maior1 = b1

if c1 > a1 and c1 > b1:
    maior1 = c1

print(f'\n       O maior valor é {maior1}\n'
      f'       E o menor valor é {menor1}')

print('\n\033[1;94m╚═══════\033[m \033[1;97mFIM DO PROGRAMA\033[m \033[1;94m═══════╝\033[m')

# --------------------------------------------------------------------------

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o menor.
menor = a  # considerando que o a é o menor.
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é o maior.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')

# --------------------------------------------------------------------------

a = int(input('Digite um número'))
b = int(input('Digite um número'))
c = int(input('Digite um número'))

menor = a  # aqui IMPLICAMOS a variável A como sendo o menor

if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c

maior = a

if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c

print(f'O menor é {menor} \n'
      f'O maior é {maior}')
