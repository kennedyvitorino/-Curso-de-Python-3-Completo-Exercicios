""" Exercício Python 004: Faça um programa que leia algo pelo
teclado e mostre na tela o seu tipo primitivo e todas
as informações possíveis sobre ele."""

algo = input('Digite algo: ')

print(f' O tipo primitivo desse valor é {type(algo)}')

print(f' Só tem espaços? {algo.isspace()}')

print(f' É numérico? {algo.isnumeric()}')

print(f' É alfabético? {algo.isalpha()}')

print(f' É alfanumérico? {algo.isalnum()}')

print(f' Está em maiúsculas? {algo.isupper()}')

print(f' Está em minusculas? {algo.islower()}')

print(f' Está capializada? {algo.istitle()}')

# --------------------------------------------------------------------------

algo = input('Digite algo')  # se o tipo não for declarado, o input sempre vai retornar uma STRING
print(f'O tipo primitivo desse valor é: \033[1;97m{type(algo)}\033[m')
print(f'Só tem espaços? \033[1;97m{algo.isspace()}\033[m')
print(f'É um número? \033[1;97m{algo.isnumeric()}\033[m')
print(f'É alfabético? \033[1;97m{algo.isalpha()}\033[m')
print(f'É alfanumérico? \033[1;97m{algo.isalnum()}\033[m')
print(f'Está em maiúsculo? \033[1;97m{algo.isupper()}\033[m')
print(f'Está em minúsculas? \033[1;97m{algo.lower()}\033[m')
print(f'Está capitalizada? \033[1;97m{algo.capitalize()}\033[m')

# --------------------------------------------------------------------------

n = str(input('Digite um Valor:'))
print(n)
print(type(n))
#
# n = float(input('Digite um VALORRR:'))
# print(n)
# print(type(n))

# --------------------------------------------------------------------------

n = bool(input('Digite um VALOR:'))
print(n)
print(type(n))

# --------------------------------------------------------------------------

n = bool(input('Digite um VALORRR:'))
print(n)
print(type(n))

# --------------------------------------------------------------------------

a = input('Digite algo: ')
print(f'Só tem espaços? {a.isspace()}')
print(f'É numérico? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')  # contem letras e números.
print(f'Está em letras maiúsculas?{a.isupper()}')
print(f'Está em letras minúsculas? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')

# --------------------------------------------------------------------------

a = input('Digite algo: ')
print(f'Só tem ESPAÇOS {a.isspace()}')
print(f'É numérico? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')  # contem letras e números.
print(f'Está  maiusculo? {a.isupper()}')
print(f'Está minusclo? {a.islower()}')
print(f'É capitaizada???? {a.istitle()}')
#
a = input('digite algo: ')
print(f'Só tem espaços? {a.isspace()}\nÉ numérico?) {a.isnumeric()}\nÉ alfabético? {a.isalpha()}\nÉ alfanumérico? {a.isalnum()}\nEstá maiuscula? {a.isupper()}\nEstá minuscula? {a.islower()}\nEstá capitalizada? {a.istitle()}')

# O "isidentifier" significa que só tem caracter alfanúmericos ou underscore_e JAMAIS
# pode ser iniciado por número ou pode conter espaços. Se respeitar isso tudo é TRUE.
# o "isprintable" significa ser printável na tela, ou seja,  se for qualquer caracter é TRUE,
# incluíndo espaço em branco. Porém, se vc usar o TAB do teclado, o resultado é FALSE.
