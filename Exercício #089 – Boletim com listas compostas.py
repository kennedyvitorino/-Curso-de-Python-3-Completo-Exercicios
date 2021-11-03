"""Crie um programa que leia nome e duas notas de
vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada
um e permita que o usuário possa mostrar as notas de
cada aluno individualmente."""


ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    resposta = str(input('Deseja continuar? {S/N] '))

    if resposta in 'Nn':
        break

print('+=' * 18)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 33)

for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 33)
    options = int(input('Mostrar notas de qual aluno? (999 para interromper): '))

    if options == 999:
        print('Finalizando...')
        break

    if options <= len(ficha) - 1:
        print(f'Notas de {ficha[options][0]} são {ficha[options][1]}')

print('<<<   Volte Sempre   >>>')
