"""Exercício Python 010: Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos dólares ela pode comprar."""

# --------------------------------------------------------------------------

print('\033[93m=' * 23)
print('  Conversão de Moedas')
print('=' * 23, '\033[m')

real = float(input('Digite aqui qualquer valor em REAIS para realizar a conversão: '))

dolar = real / 5.52    # dolar hj
euro = real / 6.37     # euro hj
eth = real / 18419.95  # ETH hoje

print(f'R${real:.2f} convertidos para dolar americano é {dolar:.2f} \n'
      f'R${real:.2f} convertidos para EURO é {euro:.2f} \n'
      f'R${real:.2f} convertidos para ETH é {eth} \n'
      f'Fim do programa.')

# --------------------------------------------------------------------------

print('\033[1;97m-------------\033[m \033[1;92mCONVERTENDO MOEDAS\033[m \033[1;97m-------------\033[m\n')

real = float(input('  Quanto de dinheiro você tem na carteira? R$'))

dolar = real / 5.15
dolar_canadense = real / 4.08
euro = real / 6.07
iene = real / 0.047

print(f'\n  Você pode converter R${real:.2f} em {dolar:.2f} dolares americano.\n'
      f'  Você pode converter R${real:.2f} em {dolar_canadense:.2f} dolares canadense,\n'
      f'  Você pode converter R${real:.2f} em {euro:.2f} EUROS.\n'
      f'  Você pode converter R${real:.2f} em {iene:.2f} ienes japonês.\n')

# --------------------------------------------------------------------------

r = float(input('•Quantos REAIS você TEM?'))

d = r / 5.63
dc = r / 4.54
e = r / 6.71
if d < 2.0:
    print(f' •Com R${r:.2f}\n •Você pode converter para {d:.2f} Centavos de Dollar Americano.')
if dc < 2.0:
    print(f' •Você pode converter para {dc:.2f} Centavos de Dollar Canadense.')
if e < 2.0:
    print(f' •Você pode converter para {e:.2f} Centavos de Euro.\n\n      •Fim do Exercício')
else:
    print(f' •Com R${r:.2f}\n •Você pode converter para {d:.2f} Dollares Americano.\n •Você pode converter para {dc:.2f} Dollares Canadense.\n •Você pode converter para {e:.2f} Euros.\n\n     •Fim do Excercício.\n      Até q enfim saiu hein maluco kkk')

# --------------------------------------------------------------------------
