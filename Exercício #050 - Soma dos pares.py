"""Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

somaP = 0
contadorP = 0
somaI = 0
contadorI = 0

for contador1 in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        somaP += numero
        contadorP += 1
    elif numero % 2 == 1:
        somaI += numero
        contadorI += 1

print(f'Você digitou {contadorP} números pares. \n'
      f'A soma deles é {somaP} \n\n'
      f'Você digitou {contadorI} números ímpares. \n'
      f'A soma deles é {somaI}')

# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m                   Soma dos pares'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m')

soma = 0
contador = 0

for c in range(1, 7):
    numero = int(input('  Digite um número: '))

    if numero % 2 == 0:  # verificando se o valor é par
        soma += numero
        contador += 1

print(f'  \nVocê digitou {contador} números pares e a soma deles é: {soma}')
print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m                  Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m')
# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m                 Soma dos ímpares'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m')

soma1 = 0
contador1 = 0

for c in range(1, 7):
    numero1 = int(input('  Digite um número: '))
    if numero1 % 2 == 1:  # verificado se o valor é ímpar.
        soma1 += numero1
        contador1 += 1

print(f'  Você digitou {contador1} números ímpares e a soma foi {soma1}')
print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m                  Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m')

# --------------------------------------------------------------------------

sum0 = 0
cont0 = 0
for c in range(1, 7):
    number0 = int(input('Informe um número: '))
    if number0 % 2 == 0:  # verificando se o valor é par
        sum0 = sum0 + number0
        cont0 = cont0 + 1
print(f'Você digitou {cont0} números -Pares- e a soma deles foi: {sum0}')

# --------------------------------------------------------------------------

# ÍMPAR.
sum1 = 0
cont1 = 0
for c in range(1, 7):
    number1 = int(input('Informe um valor: '))
    if number1 % 2:
        sum1 = sum1 + number1
        cont1 = cont1 + 1
else:
    print(f'\nVocê informou {cont1} números IMPARES e a soma foi: {sum1}')
