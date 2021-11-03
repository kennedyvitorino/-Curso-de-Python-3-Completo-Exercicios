"""Modifique as funções que foram criadas no desafio
107 para que elas aceitem um parâmetro a
mais, informando se o valor retornado por elas vai ser ou não
formatado pela função moeda(), desenvolvida no desafio 108."""

from ex109 import moeda_2

p = float(input('Digite o preço: R$'))

print('#==========#==========#==========#==========# \n'
      f'A metade de {moeda_2.moeda(p)} é {moeda_2.metade(p, True)} \n'
      f'O dobro de {moeda_2.moeda(p)} é {moeda_2.dobro(p, True)} \n'
      f'{moeda_2.moeda(p)} aumentado em 15% é {moeda_2.aumentar(p, 15, True)} \n'
      f'{moeda_2.moeda(p)} reduzido em 7% é {moeda_2.diminuir(p, 7, True)} \n'
      f'#==========#==========#==========#==========# \n'
      f'               Fim do programa \n'
      f'#==========#==========#==========#==========#')

