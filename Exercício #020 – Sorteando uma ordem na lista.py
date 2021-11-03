"""Exercício Python 20: O mesmo professor do desafio 19 quer sortear
a ordem de apresentação de trabalhos dos alunos. Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada."""
from random import shuffle


a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

lista_alunos = [a1, a2, a3, a4]

shuffle(lista_alunos)

print(f'A ordem de apresentação de trabalho será: {lista_alunos}')

# --------------------------------------------------------------------------

print(f"\n\n\033[1;91m'☼☼☼☼☼☼☼☼☼☼ Sorteando uma ordem na lista ☼☼☼☼☼☼☼☼☼☼'\033[m\n")

alu0 = str(input('Aluno 0: '))
alu1 = str(input('Aluno 1: '))
alu2 = str(input('Aluno 2: '))
alu3 = str(input('Aluno 3: '))

lista_alunos = [alu0, alu1, alu2, alu3]

# aqui será escolhida uma ordem aleatória da lista.
shuffle(lista_alunos)

print(f'A ordem de apresentação será: ')
print(lista_alunos)

# -------------------------------------------------------------------------


aluno0 = str(input('Aluno 0: '))
aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))

lista_a = [aluno0, aluno1, aluno2, aluno3]

# aqui será escolhido um nome da lista.
print(f'O aluno escolhido foi: {choice(lista_a)}')

# --------------------------------------------------------------------------
