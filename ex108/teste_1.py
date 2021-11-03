"""Adapte o código do desafio #107, criando uma função adicional
chamada moeda() que consiga mostrar os números
como um valor monetário formatado."""
from ex108 import moeda_1


p = float(input('+----------+----------+----------+----------+ \n'
                '  Digite o preço: R$'))

print('+----------+----------+----------+----------+')
print(f'  A metade de {moeda_1.moeda(p)} é {moeda_1.moeda(moeda_1.metade(p))}')
print(f'  O dobro de {moeda_1.moeda(p)} é {moeda_1.moeda(moeda_1.dobro(p))}')
print(f'  Aumentando 10%, temos {moeda_1.moeda(moeda_1.aumentar(p, 10))}')
print(f'  Diminuindo 10%, temos {moeda_1.moeda(moeda_1.subtrair(p, 10))}')
print('+----------+----------+----------+----------+')

valor = float(input('#==========#==========#==========#==========# \n'
                    '  Por favor, informe o preço: R$'))

print('#==========#==========#==========#==========# \n'
      f'  A metade de {moeda_1.moeda(valor)} é {moeda_1.moeda(moeda_1.metade(valor))}  \n'
      f'  O dobro de {moeda_1.moeda(valor)} é {moeda_1.moeda(moeda_1.dobro(valor))}  \n'
      f'  {moeda_1.moeda(valor)} aumentando 10% é {moeda_1.moeda(moeda_1.aumentar(valor, 10))}  \n'
      f'  {moeda_1.moeda(valor)} reduzido em 10% é {moeda_1.moeda(moeda_1.subtrair(valor, 10))} \n'
      f'#==========#==========#==========#==========# \n'
      f'  Fim do programa. \n'
      f'#==========#==========#==========#==========#')

