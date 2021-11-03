"""Aprimore o desafio 93 para que ele funcione com
vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador."""

jogador_dict = dict()
partidas_list = list()
time_list = list()

# lendo os dados de vários jogadores
while True:
    jogador_dict.clear()
    jogador_dict['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador_dict["nome"]} jogou? '))
    partidas_list.clear()

    for contador in range(0, total):
        partidas_list.append(int(input(f'Fez quantos gols na partida {contador + 1}? ')))

    jogador_dict['gols'] = partidas_list[:]  # copiando uma lista partidas_list completa
    jogador_dict['total'] = sum(partidas_list)  # somando o total de partidas jogadas pelo jogador
    time_list.append(jogador_dict.copy())

    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas SIM ou NAO.')
    if resposta == 'N':
        break

# Analise de dados resultante da entrada do usuário
print('▄▀' * 15)
print(' Cod ', end='')

for indice in jogador_dict.keys():
    print(f'{indice:<15}', end='')
print()
print('▄▀' * 15)

for key, valor in enumerate(time_list):
    print(f'{key:>3} ', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()
print('▄▀' * 15)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= (len(time_list)):
        print(f'ERRO! Não existe o jogador com código {busca}! ')
    else:
        print(f' »» LEVANTAMENTO DO JOGADOR {time_list[busca]["nome"]} ««')

        for indice, gols in enumerate(time_list[busca]['gols']):
            print(f'No jogo {indice + 1} fez {gols} gols.')
    print('▄▀' * 15)
print('\n  Fim do programa\n'
      '  »»» Volte Sempre «««')
