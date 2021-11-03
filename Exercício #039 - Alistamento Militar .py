"""Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele  ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo de falta ou que passou do prazo."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
from datetime import date


nome = str(input('Digite seu nome: '))

print("""\nQual é o seu sexo?
[1] para Masculino
[2] para Feminino""")

sexo = int(input('Escolha uma das alternativas acima: '))

if sexo == 1:
    print('\nVocê é homem, logo para você o alistamento é obrigatório. \n')

elif sexo != 1 and sexo != 2:
    print('Opção inválida. \n'
          'Obrigado por usar o programa!')

    quit()

else:
    print('\nVocê é mulher, logo para você o alistamento não é obrigatório. \n')

    quit()

nascimento = int(input('Em que ano você nasceu: '))

ano_atual = date.today().year
idade = ano_atual - nascimento

print(f'\nQuem nasceu em {nascimento} atualmente tem {idade} ano(s)!')

if idade == 18:
    print(f'\nVocê deve se alistar ainda este ano! \n'
          f'Boa sorte, recruta 0 !')

elif idade > 18:
    print(f'Voce já se alistou há {idade - 18 } anos atrás, no ano de {nascimento + 18}')

else:
    print(f'Você tem {idade} anos, ainda faltam {18 - idade} ano(s) para você poder se alistar! \n'
          f'Você poderá se alistar no ano de {ano_atual- (idade - 18)} .')
# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 20,
      '\n\033[1;92m                    Alisamento militar'
      )
print('\033[1;94m-=-\033[m' * 20)

nomE = str(input('\033[97m Por favor, digite seu nome: '))

print("""\n Qual é o seu gênero: 
\n [1] Feminino
 [2] masculino""")

genero = int(input('\n Escolha a opção correta de acordo com a lista acima: '))

if genero == 1:
    print('\n Você não precisa se alistar.\n'
          ' Obrigado por usar o programa!')
    print('\033[1;94m-=-\033[m' * 20,
          '\n\033[1;92m                      Fim do programa|'
          )
    print('\033[1;94m-=-\033[m' * 20)
    quit()

elif genero != 1 and genero != 2:
    print('\n Opção inválida, tente novamente!')
    print('\033[1;94m-=-\033[m' * 20,
          '\n\033[1;92m                      Fim do programa'
          )
    print('\033[1;94m-=-\033[m' * 20)
    quit()

else:
    print(' Você é homem, logo para você o alisamento é obrigatório.')

nascimento = int(input(' Qual é o ano do seu nascimento: '))

anoA = date.today().year  # aqui pegamos a data atual configurada no compiuter.
idadE = anoA - nascimento  # aqui calculamos qual é a idade do usuário pelo ano atual - data de nascimento

print(f' Quem nasceu em {nascimento} tem {idadE} ano(s) em {anoA}')

if genero == 1:
    print(' Você tem que se alistar imediatamente!')

elif idadE < 18:
    print(f' Você ainda não tem a idade necessária para o alistamento.\n'
          f' E conforme a sua idade será em {18 - idadE} ano(s).\n'
          f' No ano de {anoA + (18 - idadE)}')

else:
    print(f' Você se alistou há {idadE - 18} ano(s) atrás no ano de {anoA - (idadE - 18)}')

print('\033[1;94m-=-\033[m' * 20,
      '\n\033[1;92m                      Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 20)

# --------------------------------------------------------------------------

nome = str(input('Informe o seu nome: '))
print('''Qual é seu gênero: 
[1] Feminino
[2] Masculino''')

genero = int(input('Escolha a opção correta de acordo com a lista acima: '))
if genero == 1:
    print('Você não precisa se alistar.\nObrigado por usar o programa!')
    quit()
elif genero != 1 and genero != 2:
    print('Você usou uma opção inválida, por favor tente novamente.')
    quit()
else:
    print('Você é Homem e tem o alisamento obrigatório!')
nasci = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasci
print(f'Quem nasceu em {nasci} tem {idade} anos em {atual}')
if idade == 18:
    print('Você deve se alistar ainda este ano!')
elif idade < 18:
    print(f'Você ainda não tem a idade necessária para o alistamento,\nE conforme a sua idade será em {18 - idade} ano(s). No ano de {atual + (18 - idade)} ')
else:
    print(f'Você já se alistou há {idade - 18} ano(s) atrás \nNo ano de \033[1;31m{atual -(idade - 18)}')

# --------------------------------------------------------------------------


# cor = {'limpa':'\033[m',
#        'ver_negrito':'\033[1;31m',
#        'verm':'033[31m',
#        'verde':'\033[32m',
#        'verde_negrito':'\033[1;32m',
#        'pretoebranco':'\033[7;30m',
#        'azul':'\033[34m',
#        'azul_negrito':'\033[1;34m',
#        'negrito':'\033[1m'
#        }
atual = date.today().year
nasci = int(input(f'Ano de nascimento: '))
idade = atual - nasci
print(f'Quem nasceu em {nasci} tem {idade} anos em {atual}.')
if idade == 18:
    print(f'Você tem que se ALISTAR IMEDIATAMENTE!!!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda', 'Faltam' if saldo > 1 else 'falta', 'anos' if saldo > 1 else '1 ano', 'para o seu ALISTAMENTO.')
    ano = atual + saldo
    print(f'Seu ALISTAMENTO será em {ano}\nBoa sorte! kkk')
elif idade > 18:
    saldo = 18 - idade
    print(f'Você ja devia ter se ALISTADO\033[m há {saldo} anos')
    ano = atual - saldo

att = date.today().year
nasci = int(input(f'Em que ano você nasceu: '))
age = att - nasci
print(f'Se você nasceu no ano de {nasci}, você tem {age} anos em {att}.')
if age == 18:
    print(f' Recruta ZERO!\n ALISTE-SE IMEDIATAMENTE!')
elif age < 18:
    print(f'Teve sorte hein!?\nAinda ')
