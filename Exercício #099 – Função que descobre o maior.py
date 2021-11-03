"""Faça um programa que tenha uma função chamada
maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os
valores e dizer qual deles é o maior."""
from time import sleep


def maior(*numeros):
    contador = Maior = 0
    print('=' * 30)
    print('Analisando os valores passados...')

    for numero in numeros:
        print(f'{numero} ', end='')
        sleep(0.25)

        if contador == 0:
            Maior = numero
        else:
            if numero > Maior:
                Maior = numero
        contador += 1
    print(f'Foram informados {contador} números ao todo.')
    print(f'O maior valor informado foi: {Maior}')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(100, 500, 5856, 865, 8565, 81231, 84564, 8764, 564)
maior(1080, 500, 58656, 8365, 68565, 821231, 814564, 87364, 5642)
maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

print('\n»»» Fim do Programa «««')
