"""Faça um programa que tenha uma lista chamada
números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai
colocá-los dentro da lista e a segunda função vai
mostrar a soma entre todos os valores pares
sorteados pela função anterior."""
from random import randint
from time import sleep


def sorteia(lista_n):
    print('Sorteando 5 valores da lista: ', end='')
    for contador in range(0, 5):
        num = randint(1, 100)
        lista_n.append(num)
        print(f'{num} ', end='')
        sleep(0.2)
    sleep(0.8)
    print('\n               ► Pronto! ◄')


def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:  # se ele for divisivel por 2
            soma += valor
    print(f'Se somarmos os valores pares da lista {lista}\nteremos: {soma}')


lista_de_numeros = list()

sorteia(lista_de_numeros)
soma_par(lista_de_numeros)

# -------------------------------------------------------------------------------


def sorteio(num_lista):
    print('Sorteando 5 valores aleatórios da lista: ', end='')
    for cont in range(0, 5):
        numero = randint(0, 100)
        num_lista.append(numero)
        print(f'{numero} ', end='')
        sleep(0.25)

    sleep(0.8)
    print('\n          »» PRONTO! ««')


def soma_p(num_lista):
    soma = 0  # contador iniciando do valor 0
    for valor in num_lista:
        if valor % 2 == 0:  # Se for divisivel por 2
            soma += valor
    print(f'Somando os valores pares da lista {num_lista}\ntemos: {soma}')


lista_numeros = list()

sorteio(lista_numeros)
soma_p(lista_numeros)
