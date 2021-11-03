"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

salario_atual = float(input('Quanto você recebe por mês: '))

if salario_atual <= 1250:
    novo_salario = salario_atual + (salario_atual * 15) / 100

    print(f'Você recebia R${salario_atual:.2f} mensalmente! \n'
          f'Com o aumento de 15% você passará a receber R${novo_salario:.2f}')
else:
    novo_salario = salario_atual + (salario_atual * 10) / 100

    print(f'Você recebia R${salario_atual:.2f} mensalmente! \n'
          f'Com o aumento de 10% você passará a receber {novo_salario}')

# --------------------------------------------------------------------------

print('\n\033[1;94m╔════════\033[m \033[1;97mCALCULANDO AUMENTO NO SALÁRIO\033[m \033[1;94m════════╗\033[m\n')

salariO = float(input('    Qual é o salário do colaborador? R$'))

if salariO <= 1250:
    novoS = salariO + (salariO * 15 / 100)
    print(f'    O novo salário do colaborador é: {novoS:.2f}R$')

else:
    novoS = salariO + (salariO * 10 / 100)
    print(f'    O novo salário do colaborador é: {novoS}R$')


print('\n\033[1;94m╚═══════════════\033[m \033[1;97mFIM DO PROGRAMA\033[m \033[1;94m═══════════════╝\033[m')

# --------------------------------------------------------------------------

salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print(f'O novo salário do funcionário é: {novo:.2f}R$')
else:
    novo = salario + (salario * 10 / 100)
    print(f'O novo salário do funcionário é: {novo:.2f}R$')

# --------------------------------------------------------------------------

salario = float(input('Quanto você recebe de salário mensalmente: '))

if salario <= 1250:
    novo_salario = salario + (salario * 15) / 100
    print(f'O seu salário atual é de R${salario:.2f} \n'
          f'Agora com o aumento de 15% será de R${novo_salario}')
else:
    novo_salario = salario + (salario * 10) / 100
    print(f'Seu salário atual é de R${salario:.2f} \n'
          f'Agora com o aumento de 10% será de R${novo_salario:.2f}')
