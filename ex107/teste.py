"""Crie um módulo chamado moeda.py que tenha as
funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""
import moeda

valor = float(input('\033[1;91m+----------+----------+----------+----------+\033[m\n'
                    '\033[91m|\033[m     Por favor, informe o preço: R$'))

# print(f'\033[1;91m|----------+----------+----------+----------+\033[m\n'
#       f'\033[91m|\033[m  A metade de R${valor} é R${moeda.metade(valor):.2f}\n'
#       f'\033[91m|\033[m  O dobro de R${valor} é R${moeda.dobro(valor):.2f} \n'
#       f'\033[91m|\033[m  {valor:.2f} aumentado em 10% é R${moeda.aumentar(valor, 10):.2f}\n'
#       f'\033[91m|\033[m  {valor:.2f} diminuido em 13% é R${moeda.diminuir(valor, 13):.2f}')

print(f"""\033[91m|----------+----------+----------+----------+
\033[91m|\033[m  A metade de R${valor} é R${moeda.metade(valor):.2f}
\033[91m|\033[m  O dobro de R${valor} é R${moeda.dobro(valor):.2f} 
\033[91m|\033[m  {valor:.2f} aumentado em 10% é R${moeda.aumentar(valor, 10):.2f}
\033[91m|\033[m  {valor:.2f} diminuido em 13% é R${moeda.diminuir(valor, 13):.2f}
\033[91m|\033[m  {valor:.2f} vezes ele mesmo é igual à R${moeda.potencia(valor):.2f}

""")
