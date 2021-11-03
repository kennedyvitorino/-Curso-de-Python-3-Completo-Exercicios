"""Exercício Python 076: Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços, na sequência. No final
mostre uma listagem de preços, organizando os dados em forma tabular."""

# --------------------------------------------------------------------------

lista_produtos = ('Lápis', 1.75,
                  'Borracha', 2,
                  'Caderno', 15.90,
                  'Estojo', 25,
                  'Transferidor', 4.20,
                  'Compasso', 9.99,
                  'Mochila', 120.32,
                  'Canetas', 22.30,
                  'Livro', 34.90)
print('*' * 40)
print(f'{"Lista Básica de Material Escolar":^40}')
print('*' * 40)

for pos in range(0, len(lista_produtos)):
    if pos % 2 == 0:
        print(f'{lista_produtos[pos]:.<25}', end='')
    else:
        print(f'R${lista_produtos[pos]:>7.2f}')

print('    Fim do programa.')

# --------------------------------------------------------------------------

lista_produtos = ('Lápis', 1.75, 'Borracha', 2,
                  'Caderno', 15.90, 'Estojo', 25,
                  'Transferidor', 4.20, 'Compasso', 9.99,
                  'Mochila', 120.32, 'Canetas', 22.30,
                  'Livro', 34.90, 'Corretivo', 2.50)

print('-=' * 21)
print(f'{"Lista Básica de Material Escolar":^40}')
print('-=' * 21)

for pos in range(0, len(lista_produtos)):
    if pos % 2 == 0:
        print(f'{lista_produtos[pos]:.<30}', end='')
    else:
        print(f'{lista_produtos[pos]:.>10.2f}')

print('  Fim do programa')

# --------------------------------------------------------------------------

tupla_produtos = ('Lápis', 1.75,
                  'Borracha', 2,
                  'Caderno', 15.90,
                  'Estojo', 25,
                  'Transferidor', 4.20,
                  'Compasso', 9.99,
                  'Mochila', 120.32,
                  'Canetas', 22.30,
                  'Livro', 34.90)

print('\033[96m▀' * 25)  # Alt + 223 ▀
print(f' \033[91m{" Material Escolar Básico ":·^38}')  # Alt + 250 ·
print('\033[96m▀\033[m' * 25)

for position in range(0, len(tupla_produtos)):
    if position % 2 == 0:
        print(f'{tupla_produtos[position]:_<33}', end='')
    else:
        print(f'R${tupla_produtos[position]:>6.2f}')
print('\nFim do programa')
