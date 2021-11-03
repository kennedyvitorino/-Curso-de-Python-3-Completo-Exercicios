"""Escreva um programa que pergunte a quantidade de Km (quilômetros)
percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
R$60,00 por dia e R$015 por Km (quilômetros) rodado.
-------------------------------------------------------------------------------
FORMULA: multiplicar a quantidade de dias alugado pelo valor do
aluguel por dia (60.00 R$). depois multiplicar  a quantidade de quilômetros
rodados  pelo valor cobrado por KM  rodado (0.15 R$) e somar os 2 resultados."""


dias_aluguel = int(input('Quantos dias o carro ficou alugado: '))
km = float(input('Quantos quilômetros foram rodados: '))

pagamento = (dias_aluguel * 60) + (km * 0.15)

print(f'O carro ficou alugado em seu nome por {dias_aluguel} dia(s). \n'
      f'Foram percorridos {km:.2f}km durante os {dias_aluguel} dia(s) que você ficou com o carro alugado. \n'
      f'O valor a ser pago é de R${pagamento:.2f} \n'
      f'Fim do programa!')

# --------------------------------------------------------------------------

print('\n \033[1;97m|☼☼☼☼☼☼☼☼☼☼\033[m \033[1;91mAluguel de Carros\033[m \033[1;97m☼☼☼☼☼☼☼☼☼☼|\033[m\n\n')

aluguel_dias = int(input('Quantidade de dias que o carro ficou alugado: '))
quilometros = float(input('\nQuantos quilômetros percorridos pelo '
                          '\nveículo durante o período em que ficou alugado?'))

# fórmula: multiplicar a quantidade de dias alugado pelo valor do
# aluguel por dia (60.00 R$). depois multiplicar  a quantidade de quilômetros
# rodados  pelo valor cobrado por KM  rodado (0.15 R$) e somar os 2 resultados.
pagamento = (aluguel_dias * 60) + (quilometros * 0.15)

print(f'\nO carro ficou alugado em seu nome por {aluguel_dias} dias.\n'
      f'\nForam percorridos {quilometros}km durante os {aluguel_dias} dias que ficou alugado.'
      f'\nO valor a ser pago é de: {pagamento:.2f}R$')
# --------------------------------------------------------------------------

print('\n\n\033[1;92m========== ALUGUEL DE CARROS ==========\033[m\n')

dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km (Quilômetros) foram rodados?'))

# fórmula: multiplicar a quantidade de dias alugado pelo valor do
# aluguel por dia (60.00 R$). depois multiplicar  a quantidade de quilômetros
# rodados  pelo valor cobrado por KM  rodado (0.15 R$) e somar os 2 resultados.
pg = (dia * 60) + (km * 0.15)

print(f' •O total a pagar é de {pg:.2f}R$\n\n'
      f'\033[1;93m========== Fim do programa ==========\033[m')

# --------------------------------------------------------------------------

dia = int(input('Quantos dias alugado?'))
km = float(input('Quantos km rodados?'))

# fórmula: multiplicar a quantidade de dias alugado pelo valor do
# aluguel por dia (60.00 R$). depois multiplicar  a quantidade de quilômetros
# rodados  pelo valor cobrado por KM  rodado (0.15 R$) e somar os 2 resultados.
pg = (dia * 60) + (km * 0.15)

print(f'O Total a pagar é de: {pg:.2f}R$\n\n'
      f'\033[1;93m========== Fim do programa ==========')

# --------------------------------------------------------------------------
