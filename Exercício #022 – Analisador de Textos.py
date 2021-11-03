"""Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome."""

# --------------------------------------------------------------------------

nome = str(input('Digite seu nome: ')).strip()

print(f'Analisando o nome {nome} ... \n'
      f'Seu nome em maiúsculas: {nome.upper()} \n'
      f'Seu nome em minúsculas: {nome.lower()} \n'
      f'comprimento do seu nome: {len(nome)} \n'  # retorna o comprimento da string
      f'Seu nome tem ao todo {len(nome) - nome.count(" ")}')  # retorna o comprimento da string sem excluindo os ESPAÇOS

# --------------------------------------------------------------------------

print(f"\n\n\033[1;91m'☼☼☼☼☼☼☼☼☼☼ Analisador de textos ☼☼☼☼☼☼☼☼☼☼'\033[m\n")

n = str(input('Informe seu nome completo: ')).strip()  # strip() exclui todos os espaçoes antes e depois da string

print('Analisando seu nome...\n'
      f'Em maiúsculas é.......... {n.upper()}\n'
      f'Em minúsculas é.......... {n.lower()}\n'
      f'Seu nome tem ao todo..... {len(n)} letras\n'  # retorna o comprimento da string
      f'Seu nome tem ao todo..... {len(n) - n.count(" ")}')  # count() conta quantos espaços tem entre cada nome

separa = n.split()  # split() joga dentro de uma lista os nomes inteiros

print(f'Seu primeiro nome é...... {separa[0]}\n'
      f'E ele tem ao todo........ {len(separa[0])} letras')

# --------------------------------------------------------------------------


nome = str(input('Digite seu nome completo:'))
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)} letras')  # retorna o comprimento da string
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')  # count() conta quantos espaços tem entre cada nome
# print(f'Seu primeiro nome tem {nome.find(" ")} letras')
separador = nome.split()  # split() separa cada palavra da string e transforma em lista.
print(f'Seu primeiro nome é {separador[0]} e ele tem {len(separador[0])} letras.')

