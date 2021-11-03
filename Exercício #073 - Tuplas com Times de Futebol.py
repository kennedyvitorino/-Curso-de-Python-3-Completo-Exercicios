"""Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros
colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

# --------------------------------------------------------------------------

times = 'Atletico-MG', 'Palmeiras', 'Flamengo', 'Fortaleza',\
        'Bragantino', 'Corinthians', 'Internacional', 'Flluminense',\
        'Cuiabá', 'Athletico-PR', 'Sao Paulo', 'Ceara SC',\
        'Santos', 'Bahia', 'Juventude', 'Gremio',\
        ' america-MG', 'Sport Recife', 'Vasco', 'Chapecoense'

print(f'Os cinco primeiros colocados são:\n{times[:5]}\n')  # mostre os 5 primeiros colocados
print(f'Os quatro últimos colocados são:\n{times[-4:]}\n')  # mostre os últimos 4 colocados
print(f"Os times em ordem alfabética são:\n{sorted(times)}\n")  # mostrar em ordem alfabética
print(f'O último colocado é: {times[-1]}')
print(f'O Chapecoense está na posição {times.index("Chapecoense")} ')  # mostrar o último time [Chapecoense]

# --------------------------------------------------------------------------
