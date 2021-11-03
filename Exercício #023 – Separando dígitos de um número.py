"""Exercício Python 23: Faça um programa que
leia um número de 0 a 9999 e mostre na tela
cada um dos dígitos separados."""

numero = int(input('Digite um número: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f' Você digitou {numero}\n'
      f'Unidade {unidade} \n'
      f'Dezena {dezena} \n'
      f'Centena {centena} \n'
      f'Milhar {milhar}')

# --------------------------------------------------------------------------

print(f"\n\n\033[1;91m'☼☼☼☼☼☼☼☼☼☼ Separando dígitos de um número ☼☼☼☼☼☼☼☼☼☼'\033[m\n")

num = int(input('        Digite um valor a ser tratado: '))

unid = num // 1 % 10  # 1º ordem
deze = num // 10 % 10  # 2º ordem
cent = num // 100 % 10  # 3º ordem

milhar = num // 1000 % 10

uni_milhar = num // 10000 % 10  # 4º ordem
dez_milhar = num // 100000 % 10  # 5º ordem
cen_milhar = num // 1000000 % 10  # 6º ordem

uni_milhao = num // 10000000 % 10  # 7º ordem
dez_milhao = num // 100000000 % 10  # 8º ordem
cen_milhao = num // 1000000000 % 10  # 9º ordem

uni_milhares = num // 10000000000 % 10  # 10º ordem
dez_milhares = num // 100000000000 % 10  # 11º ordem
cen_milhares = num // 1000000000000 % 10  # 12º ordem

print(f'\n        Você inseriu {len(str(num))} digitos.\n')

print(f'        Analisando o número... {num}\n\n'
      f'        Unidade:............................ {unid}\n'
      f'        Dezena:............................. {deze}\n'
      f'        Centena:............................ {cent}\n'
      f'        Milhar:............................. {milhar}\n\n'

      f'        Unidade de milhar:.................. {uni_milhar}\n'
      f'        Dezena de milhar:................... {dez_milhar}\n'
      f'        Centena de milhar:.................. {cen_milhar}\n\n'

      f'        Unidade de milhão:.................. {uni_milhao}\n'
      f'        Dezena de milhão.................... {dez_milhao}\n'
      f'        Centena de milhão:.................. {cen_milhao}\n\n'

      f'        Unidade de milhares:................ {uni_milhares}\n'
      f'        Dezena de milhares:................. {dez_milhares}\n'
      f'        Centena de milhares:................ {cen_milhares}\n\n'
      f'            \033[1;92m♦♦♦♦♦♦♦♦♦♦ Fim do programa ♦♦♦♦♦♦♦♦♦♦\033[m'
      )

# --------------------------------------------------------------------------


numero = int(input('        Informe um número:'))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
unidade_milhar = numero // 10000 % 10
dezena_milhar = numero // 100000 % 10
centena_milhar = numero // 1000000 % 10
print(f'\n        Analisando o número: {numero}')
print(f'        Unidade: {unidade}')
print(f'        Dezena: {dezena}')
print(f'        Centena: {centena}')
print(f'        Milhar: {milhar}')
print(f'        Unidade de milhar: {unidade_milhar}')
print(f'        Dezena de milhar: {dezena_milhar}')
print(f'        Centena de milhar: {centena_milhar}')

# --------------------------------------------------------------------------
