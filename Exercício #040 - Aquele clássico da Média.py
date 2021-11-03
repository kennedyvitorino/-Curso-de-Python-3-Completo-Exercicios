"""Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem nofinal, de acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO"""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'A média do aluno foi {media} \n'
          f'{"REPROVADO!": ^20}')
elif media == 5 or media <= 6.9:
    print(f'A média do aluno foi {media} \n'
          f'{"Recuperação": ^20}')
else:
    print(f'A média do aluno foi {media} \n'
          f'{"Aprovado!": ^20}')

# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 15,
      '\n\033[97m             Calculando a média'
      )
print('\033[1;94m-=-\033[m' * 15)

nota1 = float(input('\n\033[97m Informe a primeira nota:...'))
nota2 = float(input(' Informe a segunda nota:....'))

media = float(nota1 + nota2) / 2

if 7 > media >= 5:
    print(f' Sua média é {media:.1f} e você está em recuperação!\n')

elif media < 5:
    print(f' Sua média é {media:.1f} e você foi reprovado!\n')

elif media >= 7:
    print(f' Sua média é {media:.1f}\n'
          ' Você foi aprovado!\n')

print('\033[1;94m-=-\033[m' * 15,
      '\n\033[97m             Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 15)
# --------------------------------------------------------------------------

number1 = float(input('Informe a primeira nota: '))
number2 = float(input('Informe a segunda nota: '))
media = float(number1 + number2) / 2
if 7 > media >= 5:
    print(f'Sua média é {media:.1f} e você está em \033[1;33mRecuperação!\033[m')
elif media < 5:
    print(f'Sua media é {media:.1f} e você foi \033[1;31mReprovado!\033[m')
elif media >= 7:
    print(f'Sua média é {media} e você foi \033[1;35mAprovado!!!')
