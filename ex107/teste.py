"""Crie um módulo chamado moeda.py que tenha as
funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""
import moeda
from linha import *

print(linha())

valor = float(input('          Por favor, informe o preço: R$'))

cabecalho('CONFIRA O RESULTADO LOGO ABAIXO.')

print(f"""{linha()}
  A metade de R${valor} é R${moeda.metade(valor):.2f}
  O dobro de R${valor} é R${moeda.dobro(valor):.2f} 
  {valor:.2f} aumentado em 10% é R${moeda.aumentar(valor, 10):.2f}
  {valor:.2f} diminuido em 13% é R${moeda.diminuir(valor, 13):.2f}
  {valor:.2f} vezes ele mesmo é igual à R${moeda.potencia(valor):.2f}
""")

