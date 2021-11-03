"""Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou. Depois vai
ler a quantidade de gols feitos em cada partida. No
final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato."""

jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for cont in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {cont + 1}? ')))

jogador['gols'] = partidas[:]  # copiando a lista partidas
jogador['total'] = sum(partidas)  # somando o total das partidas do jogador

print('-' * 45)
print(jogador)
print('-' * 45)

for key, valor in jogador.items():
    print(f'O campo {key} tem o valor {valor}')

print('-' * 45)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for indice, valor in enumerate(jogador['gols']):
    print(f'→ Na partida {indice + 1}, fez {valor} gols.')
