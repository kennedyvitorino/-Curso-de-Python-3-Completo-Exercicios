""" Exercício Python 071: Crie um programa que simule o
funcionamento de um caixa eletrônico. No início, pergunte
ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. """
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# Alt + 186 ║
# --------------------------------------------------------------------------

print('\033[97m╔════════════════════════════════════╗'
      '\n║          \033[1;7;91mPrimordial Bank\033[m\033[97m           ║ \n'
      '╚════════════════════════════════════╝\n\033[m\033[97m')

valor = int(input(' Qual valor você deseja sacar hoje? R$'))
total = valor
cedula = 200
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1

    else:
        if total_cedulas > 0:
            print(f' O total de {total_cedulas} cédulas de R${cedula}')

        if cedula == 200:
            cedula = 100

        elif cedula == 100:
            cedula = 50

        elif cedula == 50:
            decula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            decula = 5

        elif cedula == 5:
            cedula = 2

        total_cedulas = 0

        if total == 0:
            break

# --------------------------------------------------------------------------


print('\033[1:36m=\033[m' * 25)
bank = '\033[1:7:30mDKVS BANK\033[m'
print(f'{bank:^37}')
print('\033[1:36m=\033[m' * 25)

value = int(input(' Qual valor você quer sacar? R$'))
total = value
cedula = 200
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f' Total de {totcedula} cédulas de R${cedula}')
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        totcedula = 0
        if total == 0:
            break
print('\033[1:36m=\033[m' * 45)
print(' Volte sempre ao DKVS BANK! Tenha um bom dia!')
print('\033[1:36m=\033[m' * 45)

# lembrar de adicionar mais as CÉDULAS  de 2, 5, 100 reais (condicionais)
