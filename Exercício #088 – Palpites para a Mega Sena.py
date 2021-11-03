"""Faça um programa que ajude um jogador da MEGA SENA
a criar palpites.O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para
cada jogo, cadastrando tudo em uma lista composta."""
from random import randint
from time import sleep

megasena_lista = list()
jogos_lista = list()

print('=+' * 20)
print('           Joga na MEGASENA     ')
print('=+' * 20)

quanti = int(input('Quantos jogos você quer sortear? '))

tot_jogos = 1

while tot_jogos <= quanti:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in megasena_lista:
            megasena_lista.append(num)
            cont += 1
        if cont >= 6:
            break

    megasena_lista.sort(), jogos_lista.append(megasena_lista[:]), megasena_lista.clear()
    tot_jogos += 1

sleep(0.5)

print('+=' * 3, f' Sorteando {quanti} Jogos ', '+=' * 3)

for i, l in enumerate(jogos_lista):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.5)

print('\n   <====# Boa Sorte #====>')
