"""Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função
nput() do Python, só que fazendo a validação
para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)"""


def leiaint(msg):
    ok = False
    valor = 0

    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[1;91m__________________________________________'
                  '\n  ERRO! digite um número inteiro válido!\n'
                  '──────────────────────────────────────────\033[m')
        if ok:
            return valor


# Programa Principal
numero = leiaint('Digite um número:')
print(f'Você acabou de digitar o número {numero}')
