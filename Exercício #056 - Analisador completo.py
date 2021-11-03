"""Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é
o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m                 Analisador completo'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

soma_idade = 0
media_idade = 0
maior_idadehomem = 0
nome_velho = ' '
tot_mulher20 = 0

for pessoa in range(1, 5):
    print(f' {pessoa}ª pessoa')
    nome = str(input(' Seu nome: ')).strip()
    idade = int(input(' Sua idade: '))
    sexo = str(input(' Seu gênero [M/F]: ')).strip()

    soma_idade += idade

    if pessoa == 1 and sexo in 'Mm':
        maior_idadehomem = idade
        nome_velho = nome

    if sexo in 'Mm' and idade > maior_idadehomem:
        maior_idadehomem = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        tot_mulher20 += 1

media_idade = soma_idade / 4

print(f' A faixa etária do grupo é: {media_idade}\n'
      f' O mais velho tem {maior_idadehomem} anos e seu nome é {nome_velho}\n'
      f' Ao todo são {tot_mulher20} mulheres com menos de 20 anos.\n')

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m                 Analisador completo'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

# --------------------------------------------------------------------------


somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'=-{p}ª')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'mM' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'fF' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4

print(f'A faixa etária do grupo é: {mediaidade}')
print(f'O mais mais velho tem {maioridadehomem} anos e seu nome é {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')

# somaidade = 0
# mediaidade = 0
# maioridadehomem = 0
# nomevelho = ''
# totmulher20 = 0
# for p in range(1, 5):
#     print(f'\033[1;31m→→→→→→\033[m {p}ª pessoa \033[1;31m←←←←←←\033[m')
#     nome = str(input('Nome: ')).strip()
#     idade = int(input('Idade: '))
#     sexo = str(input('Sexo [M/F]')).strip()
#     somaidade += idade
#     if p == 1 and sexo in 'Mm':
#         maioridadehomem = idade
#         nomevelho = nome
#     if sexo in 'Mm' and idade > maioridadehomem:
#         maioridadehomem = idade
#         nomevelho = nome
#     if sexo in 'Ff' and idade < 20:
#         totmulher20 += 1
# mediaidade = somaidade / 4
# print(f'A média de idade do grupo é de {mediaidade} anos.')
# print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
# print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')

# somaidade = 0
# mediaidade = 0
# maioridadehomem = 0
# nomevelho = ''
# totmulher20 = 0
# for p in range(1, 5):
#     print(f'-----{p}ª pessoa -----')
#     nome = str(input('Nome: ')).strip()
#     idade = int(input('Idade: '))
#     sexo = str(input('Sexo [ M / F ]')).strip()
#     somaidade += idade
#     if p == 1 and sexo in 'Mm':
#         maioridadehomem = idade
#         nomevelho = nome
#     if sexo in 'Mm' and idade > maioridadehomem:
#         maioridadehomem = idade
#         nomevelho = nome
#     if sexo in 'Ff' and idade < 20:
#         totmulher20 += 1
# mediaidade = somaidade / 4
# print(f'A média de idade do grupo é de {mediaidade} anos.')
# print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
# print(f'A todo são {totmulher20} mulheres com menos de 20 anos.')

# somaidade = 0
# mediaidade = 0
# maioridadehomem = 0
# nomevelho = ''
# totmulher20 = 0
# for p in range(1, 5):
#     print(f'-----{p}ª pessoa -----')
#     nome = str(input('Nome: ')).strip()
#     idade = int(input('Idade: '))
#     sexo = str(input('Sexo [ M / F ]')).strip()
#     somaidade += idade
#     if p == 1 and sexo in 'Mm':
#         maioridadehomem = idade
#         nomevelho = nome
#     if sexo in 'Mm' and idade > maioridadehomem:
#         maioridadehomem = idade
#         nomevelho = nome
#     if sexo in 'Ff' and idade < 20:
#         totmulher20 += 1
# mediaidade = somaidade / 4
# print(f'A média de idade do grupo é de {mediaidade} anos.')
# print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
# print(f'A todo são {totmulher20} mulheres com menos de 20 anos.')
