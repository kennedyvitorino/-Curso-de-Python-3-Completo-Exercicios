"""Exercício Python 16: Crie um programa que leia
um número Real qualquer pelo teclado e mostre
na tela a sua porção Inteira.
Ex: digite um número: 6.4532
o número 6.4532 tem a parte inteira 6."""
from math import trunc

numero = float(input('Digite um valor: '))

print(f'o valor digitado foi {numero} \n'
      f'e sua parte inteira é {trunc(numero)}')

# --------------------------------------------------------------------------

print(f'Crie um programa que leia umnúmero real qualquer\n'
      f' pelo teclado e mostre na tela a sua posição inteira.')
# --------------------------------------------------------------------------

numero = float(input(' Digite um valor: '))

# usando método TRUNC para retornar apenas a parte inteira de um número.
print(f'O valor digitado foi {numero} e a sua porção inteira é: {trunc(numero)}\n')

# --------------------------------------------------------------------------

print(f'\n Crie um programa que leia um nº real qualquer pelo teclado e\n'
      f'mostre na tela sua posição inteira.')

# --------------------------------------------------------------------------

numero = float(input('Diga um valor: '))

# usando método TRUNC para retornar apenas a parte inteira de um número.

print(f'O valor digitado foi {numero} e a sua porção inteira é: {trunc(numero)}\n')

# --------------------------------------------------------------------------

# modo de fazer o mesmo programa sem importar a lib math
numero = float(input('Informe um valor: '))

# usando método TRUNC para retornar apenas a parte inteira de um número.
print(f'O Valor informado foi {numero} e a sua posição inteira é: {int(numero)}')

# --------------------------------------------------------------------------
