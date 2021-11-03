"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

peso = float(input('Por favor, digite o seu peso: '))
altura = float(input('Por favor, digite a sua estatura: '))

IMC = peso / (altura ** 2)

if IMC <= 18.5:
    print(f'Seu imc é {IMC:.2f}! Você está abaixo do peso!')
elif IMC <= 25:
    print(f'Seu imc é {IMC:.2f}! Você está no peso ideal!')
elif IMC <= 30:
    print(f'Seu imc é {IMC:.2f}! Você está com sobrepeso!')
elif IMC <= 40:
    print(f'Seu imc é {IMC:.2f}! Você está em obesidade!')
else:
    print(f'Seu imc é {IMC:.2f}! Você está em obesidade morbida!')

# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 22,
      '\n\033[97m             Calculando o índice de massa corporea'
      )
print('\033[1;94m-=-\033[m' * 22)

pes0 = float(input('\n\033[97m Qual é o seu peso? (Kg).....'))
altur4 = float(input(' Qual é a sua altura? (m)....'))

IMC = pes0 / altur4 ** 2

if IMC < 18.5:
    print(f'\n Seu Índice de Massa Corporea é {IMC:.2f} e você está abaixo do peso!\n')

elif 18.5 <= IMC < 25:
    print(f'\n Seu Índice de Massa Corporea é {IMC:.2f} e você está no peso normal!\n')

elif 25 <= IMC < 30:
    print(f'\n Seu Índice de Massa Corpea é {IMC:.2f} e você está com sobrepeso!\n')

elif 30 <= IMC < 40:
    print(f'\n Seu IMC é {IMC:.2f} e você está em obesidade! Procure se cuidar!\n')

elif IMC >= 40:
    print(f'\n Seu Índice de Massa Corporea é {IMC:.2f}\n'
          f' E está em obesidade morbida!\n'
          f' Procure um médico urgentemente!!!\n')

print('\033[1;94m-=-\033[m' * 22,
      '\n\033[97m                        Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 22)
# --------------------------------------------------------------------------

peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.2f} e você está no peso normal!')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.2f} e você está com SOBREPESO, Vamos malhar jovem!')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.2f} e você está em OBESIDADE! Procure se cuidar!')
elif imc >= 40:
    print(f'Seu IMC é {imc} e você está em OBESIDADE MORBIDA! PROCURE UM MÉDICO URGENTEMENTE!')


# peso = float(input('Qual é o seu peso? (kg)
# altura = float(input('Qual é sua altura? (m) '))
# imc = peso / altura ** 2
# print(f'O seu IMC é: {imc:.2f}')
# if imc < 18.5:
#     print('Você está ABAIXO DO PESO normal!')
# elif 18.5 <= imc < 25:
#     print('Parabéns, você está na faixa de PESO normal.')
# elif 25 <= imc < 30:
#     print('Você está em SOBREPESO, vá malhar home.. kkkkjkjk')
# elif 30 <= imc < 40:
#     print('Você está em OBESIDADE, procure se cuidar!')
# elif imc >= 40:
#     print('Você está em OBESIDADE MORBIDA!, cuidado!')




