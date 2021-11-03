"""Adapte o código do desafio #107, criando uma função adicional
chamada moeda() que consiga mostrar os números
como um valor monetário formatado."""


def aumentar(price, taxa):
    res = price + (price * taxa / 100)
    return res


def subtrair(price, taxa):
    res = price - (price * taxa / 100)
    return res


def dobro(price):
    res = price * 2
    return res


def metade(price):
    res = price / 2
    return res


def moeda(price=0, moeda1='R$'):  # função que formata moeda com VÍRGULA ao invés de PONTO
    return f'{moeda1}{price:>7.2f}'.replace('.', ',')
