"""Exercício Python 57: Faça um programa que leia o sexo
de uma pessoa,mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação
novamente até ter um valor correto. """
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m                   Validando dados'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

sex = str(input(' Informe o seu gênero: \033[1m[M/F]\033[m\033[97m')).strip().upper()[0]

while sex not in 'MmFf':
    sex = str(input(' Dados inválidos.\n'
                    ' Por favor, informe seu sexo: ')).strip().upper()[0]

print(f' Gênero registrado com sucesso!\n')
print('\033[1;92m-=-\033[m' * 18,
      '\n\033[97m                 Fim do programa'
      )
print('\033[1;92m-=-\033[m' * 18, '\n\033[97m')

# --------------------------------------------------------------------------


sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos.\nPor favor, informe seu sexo: ')).strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso.')
