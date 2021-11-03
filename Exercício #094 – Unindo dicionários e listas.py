"""Exercício Python 094: Crie um programa que leia nome,
sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários
em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""


# recebendo dados pelo teclado e cadastrando em lista e dicionario.
pessoa_dict = dict()
galera_list = list()

soma = media = 0  # CONTADORES

while True:
    pessoa_dict.clear()  # limpa a o dicionário a cada volta completa no LOOPING
    pessoa_dict['nome'] = str(input('Informe o seu nome: '))

    while True:
        pessoa_dict['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa_dict['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa_dict['idade'] = int(input('Informe a sua idade: '))
    soma += pessoa_dict['idade']
    galera_list.append(pessoa_dict.copy())

    while True:
        resposta = str(input('Você deseja continuar? [S/N]')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas SIM ou NÃO.')
    if resposta == 'N':
        break

# analisando os resultados dos dados que foram colocados na lista pelo código acima.
print('▄ ' * 15)
print(f'A) Ao todo temos {len(galera_list)} pessoas cadastradas.')

media = soma / len(galera_list)

print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')

for pessoa in galera_list:
    if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]} ', end='')
print()

print('D) Lista das pessoas que estão acima da média:')

for pessoa in galera_list:
    if pessoa['idade'] >= media:
        print('     ')
        for key, valor in pessoa.items():
            print(f'{key} = {valor}; ', end='')
        print()
print(' <<< Encerrado >>> ')
