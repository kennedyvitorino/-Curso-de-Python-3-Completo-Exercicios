""" Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
agora a possibilidade da digitação de um número de tipo
inválido. Aproveite e crie também uma função leiaFloat()
com a mesma funcionalidade."""


def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):  # tratamento de exceções
            print('\033[91m Erro: por favor digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(' Entrada de dados interrompida pelo usuário')
        else:
            return numero


def leia_float(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):  # tratamento de exceções
            print('\033[91m ERRO: por favor digite um real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(' Entrada de dados interrompida pelo usuário')
        else:
            return numero


num_int = leia_int(' Digite um número inteiro: ')
num_float = leia_float(' Digite um número real: ')
print(f' O número inteiro digitado foi {num_int} \n'
      f' O número real digitado foi {num_float}')
