"""A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
from datetime import date

nascimento = int(input('Data de nascimento: '))

anoAtual = date.today().year

idade = anoAtual - nascimento

if idade <= 9:
    print(f'Você tem {idade} anos, e está na categoria Mírim!')
elif idade <= 14:
    print(f'Você tem {idade} anos, e está na categoria Infantil!')
elif idade <= 19:
    print(f'Você tem {idade} anos, e está na categoria Junior!')
elif idade <= 25:
    print(f'Você tem {idade} anos, e está na categoria Sênior!')
else:
    print(f'Você tem {idade} anos, e está na categoria Master!')

# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 20,
      '\n\033[97m                   Categoria de atletas'
      )
print('\033[1;94m-=-\033[m' * 20)

data_atual = date.today().year
nasci = int(input('\n\033[97m Qual o ano do seu nascimento?'))
idadE = data_atual - nasci

if idadE <= 9:
    print(f' Você tem {idadE} anos, portanto percente a categoria mirim!')

elif idadE <= 14:
    print(f' Você tem {idadE} anos, portanto pertence a categoria infantil!')

elif idadE <= 19:
    print(f' Você tem {idadE} anos, portanto pertence a categoria junior!')

elif idadE <= 25:
    print(f' Você tem {idadE} anos, portanto pertence a categoria sênior!')

else:
    print(f' Você tem {idadE} anos, portanto pertence a categoria master!')


print('\033[1;94m-=-\033[m' * 20,
      '\n\033[97m                   Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 20)

# --------------------------------------------------------------------------

ano_atual = date.today().year
nascimento = int(input('Ano do seu Nascimento: '))
idade = ano_atual - nascimento
if idade <= 9:
    print(f'você tem {idade} anos, portanto pertence a categoria MIRIM!')
elif idade <= 14:
    print(f'Você tem {idade} anos, portanto pertence a categoria INFANTIL!')
elif idade <= 19:
    print(f'Você tem {idade} anos, portanto pertence a categoria JUNIOR!')
elif idade <= 25:
    print(f'Você tem {idade} anos, portanto pertence a categoria SÊNIOR!')
else:
    print(f'Voc tem {idade} anos, portanto pertence a categoria MASTER!')
