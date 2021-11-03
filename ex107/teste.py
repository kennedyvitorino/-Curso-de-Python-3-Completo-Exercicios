"""Crie um módulo chamado moeda.py que tenha as
funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""
import moeda


vlr = float(input('Informe o preço: R$'))

print(f'A metade de R${vlr:.2f} é R${moeda.metade(vlr):.2f} \n'
      f'O dobro de R${vlr:.2f} é R${moeda.dobro(vlr):.2f} \n'
      f'R${vlr:.2f} aumentado em 50% é R${moeda.aumentar(vlr, 50):.2f} \n'
      f'R${vlr:.2f} reduzido em 38% é R${moeda.diminuir(vlr, 38):.2f} \n'
      f'Fim do programa')

# --------------------------------------------------------------------------------

valor = float(input('\033[1;91m+----------+----------+----------+----------+\033[m\n'
                    '\033[91m|\033[m  Por favor, informe o preço: R$'))

print(f'\033[1;91m|----------+----------+----------+----------+\033[m\n'
      f'\033[91m|\033[m  A metade de R${valor} é R${moeda.metade(valor):.2f}\n'
      f'\033[91m|\033[m  O dobro de R${valor} é R${moeda.dobro(valor):.2f} \n'
      f'\033[91m|\033[m  {valor:.2f} aumentado em 10% é R${moeda.aumentar(valor, 10):.2f}\n'
      f'\033[91m|\033[m  {valor:.2f} diminuido em 13% é R${moeda.diminuir(valor, 13):.2f}')

# --------------------------------------------------------------------------------

p = float(input('\033[1;91m+----------+----------+----------+----------+\033[m\n'
                '\033[1;91m|\033[m  Digite o preço: R$'))

print('\033[1;91m|----------+----------+----------+----------+\033[m')
print(f'\033[91m|\033[m  A metade de R${p} é R${moeda.metade(p):.2f}')
print(f'\033[1;91m|\033[m  O dobro de R${p} é R${moeda.dobro(p):.2f}')
print(f'\033[1;91m|\033[m  Aumentando 10%, temos R${moeda.aumentar(p, 10):.2f}')
print(f'\033[1;91m|\033[m  Diminuindo 10%, temos R${moeda.diminuir(p, 10):.2f} \n'
      f'\033[1;91m+----------+----------+----------+----------+ ')
