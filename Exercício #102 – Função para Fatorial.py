def fatorial(numero, show=False):
    """
    \033[97m»» Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor do Fatorial de um número numero. \033[m
    """

    fat = 1

    for contador in range(numero, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print('\033[1;93m x \033[m', end='')
            else:
                print('\033[1;93m = \033[m', end='')

        fat *= contador
    return fat


# Programa Principal
fatoriaL = int(input('Digite um número para ver o seu Fatorial: '))

print(fatorial(fatoriaL, show=True))

help(fatorial)
