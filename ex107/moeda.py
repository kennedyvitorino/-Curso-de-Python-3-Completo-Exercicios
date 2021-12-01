"""Crie um módulo chamado moeda.py que tenha as
funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""
# funçoes usadas para criação do MODULO


def aumentar(price, taxa):
    res = price + (price * taxa / 100)
    return res


def diminuir(price, taxa):
    res = price - (price * taxa / 100)
    return res


def dobro(price):
    res = price * 2
    return res


def metade(price):
    res = price / 2
    return res


def potencia(price):
    res = price ** 2
    return res
