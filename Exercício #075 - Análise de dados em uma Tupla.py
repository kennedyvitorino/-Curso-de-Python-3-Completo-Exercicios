"""Exercício Python 075: Desenvolva um programa que
leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

valor = (int(input('Digite  um valor: ')),
         int(input('Digite  outro valor: ')),
         int(input('Digite  mais um valor: ')),
         int(input('Digite  o último valor: ')))

print(f'\nVocê digitou os valores {valor} \n'
      f'O valor 9 apareceu {valor.count(9)}')

if 3 in valor:
    print(f'O valor 3 apareceu na {valor.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')

for v in valor:
    if v % 2 == 0:
        print(v, end=' ')

# --------------------------------------------------------------------------
