"""Faça um programa que calcule a soma entre
todos os números que são múltiplos de três e
que se encontram no intervalo de 1 até 500. """
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

soma_total = 0
contador = 0

for contador1 in range(1, 501, 2):
    if contador1 % 3 == 0:
        contador += 1
        soma_total += contador1

print(f'A soma de todos os {contador} múltiplos de 3 é igual a {soma_total}')

# --------------------------------------------------------------------------

contador = 0
soma = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1
print(f'\nTodos os múltiplos de 3 até no intervalo de de 1 até 500 são: \n'
      f'Múltiplos de 3 encontrados: {contador} \n'
      f'Soma de todos eles: {soma}')

# --------------------------------------------------------------------------

cont = 0
soma_total = 0

for contador in range(1, 501, 2):
    if contador % 3 == 0:
        soma_total += contador
        cont += 1
print(f'Somando todos os {cont} valores solicitados temos {soma_total}')

# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m          Somando ímpares multiplos de três'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m')

acu_soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        acu_soma += c
        cont += 1

print(f'  A soma de todos os {cont} valores solicitados é {acu_soma}')
print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m                  Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m')

# --------------------------------------------------------------------------

# acumulador_soma = 0
# contador = 0
# for variavel_controle in range(1, 501, 2):
#     if variavel_controle % 3 == 0:
#         acumulador_soma = acumulador_soma + variavel_controle
#         contador = contador + 1
# print(f'\033[1;34mA soma de todos os\033[m {contador} \033[1;34mvalores solicitados é:\033[m {acumulador_soma}')
#
# soma = 0
# cont = 0
# for variavel_controle in range(1, 501, 2):
#     if variavel_controle % 3 == 0:
#         soma += variavel_controle
#         cont += 1
# print(f'\033[1;32mA soma de todos os\033[m {cont} \033[1;32mvalores solicitados é:\033[m {soma}')
#
# soma = 0
# conta = 0
# for c in range(1, 501, 2):
#     if c % 3 == 0:
#         soma = soma + c
#         conta = conta + 1
# print(f'A soma de todos os {conta} valores é {soma}')
