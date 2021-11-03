"""Exercício Python 19: Um professor quer sortear um dos seus
quatro alunos para apagar o quadro. Faça um programa que
ajude ele, lendo o nome dos alunos e escrevendo na tela
o nome do escolhido."""

from random import choice

n1 = str(input('1ª aluno:...'))
n2 = str(input('2ª aluno:...'))
n3 = str(input('3ª aluno:...'))
n4 = str(input('4ª aluno:...'))


lista_sorteio = [n1, n2, n3, n4]

# premiado = choice(lista_sorteio)

print(f'\nO aluno(a) premiado(a) foi {choice(lista_sorteio)} \n'
      f'Fim do programa!')

# --------------------------------------------------------------------------

print(f"\n\n\033[1;91m'☼☼☼☼☼☼☼☼☼☼ Sorteando um item na lista ☼☼☼☼☼☼☼☼☼☼'\033[m\n")

n0 = str(input('    Primeiro aluno: '))
n1 = str(input('    Segundo aluno:  '))
n2 = str(input('    Terceiro aluno: '))
n3 = str(input('    Quarto aluno:   '))

lista0 = [n0, n1, n2, n3]

escolhido0 = choice(lista0)

print(f'\n    O aluno(a) premiado foi o(a) {choice(lista0)}')

# --------------------------------------------------------------------------

