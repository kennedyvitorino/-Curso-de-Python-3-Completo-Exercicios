""" Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá ser capaz
de mostrar a ficha do jogador, mesmo que algum dado não
tenha sido info rmado corretamente."""


def ficha(nome_j='<Desconhecido>', quant_gol=0):
    print(f'O jogador {nome_j} fez {quant_gol} gol(s) no decorrer de todo o campeonato.')


# Programa Principal
nome = str(input('Nome do jogador:...... '))
gols = str(input('Número de gols:....... '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(quant_gol=gols)
else:
    ficha(nome, gols)
