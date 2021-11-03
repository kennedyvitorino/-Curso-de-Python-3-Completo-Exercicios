"""Exercício Python 077: Crie um programa que tenha uma tupla com várias
palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais."""
# ----------------------------------------------------

palavras = 'aprender', 'programar', 'linguagem', 'python', \
           'curso', 'gratis', 'estudar', 'praticar', \
           'trabalhar', 'mercado', 'programador', 'futuro'

for palavra in palavras:
    print(f'\n Na palavra \033[91m{palavra.upper()}\033[m temos ', end='')

    for letra in palavra:

        if letra.lower() in 'aeiou':
            print(f'\033[91m{letra.upper()}\033[m', end=' ')

# ----------------------------------------------------

palavras = 'aprender', 'programar', 'linguagem', 'python', \
           'curso', 'gratis', 'estudar', 'praticar', \
           'trabalhar', 'mercado', 'programador', 'futuro'

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra.upper()}', end=' ')
