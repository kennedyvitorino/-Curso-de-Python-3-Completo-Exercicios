"""Faça um programa que tenha uma função chamada
escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:escreva(‘Olá, Mundo!’)
Saída:~~~~~~~~~
     Olá, Mundo!
      ~~~~~~~~~"""


def escreva(msg):
    tam = len(msg) + 4

    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Davyd Kennedy Vitorino')
escreva('Curso d Python no YouTube')
escreva('CeV')
escreva('O rato roeu a roupa do Rei de Roma.')

# --------------------------------------------------------------------------


def escreva(msg):
    tam = len(msg) + 4
    print('\033[1;94m=\033[m' * tam)
    print(f'  \033[93m{msg}')
    print('\033[1;94m=\033[m' * tam)


# Programa Principal
escreva('Davyd Kennedy Vitorino da Silva Dantas')
escreva('Sonally Cecília Dantas Sales Vitorino')
escreva('Belchior Vitorino Dantas')
escreva('Jesus humilha o satanás')
