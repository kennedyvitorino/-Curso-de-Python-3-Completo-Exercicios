""" Faça um programa que leia nome e média de
um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da
estrutura na tela."""

aluno = dict()

aluno['Nome'] = str(input('Digite seu nome social: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}'))

if aluno['Média'] >= 7:
    aluno['Situção'] = 'Aprovado!'

elif aluno['Média'] <= 5:
    aluno['Sitação'] = 'Em Recuperação!'

else:
    aluno['Situação'] = 'Reprovado!'

print('+=' * 22)

for k, v in aluno.items():
    print(f'☼ {k} é {v}')

print(aluno)
