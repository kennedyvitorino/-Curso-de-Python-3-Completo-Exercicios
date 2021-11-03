
"""Exercício Python 18: Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""


# importando apenas os métodos que serão usados
from math import radians, sin, tan, cos


# --------------------------------------------------------------------------

print(f"\n\n\033[1;91m'☼☼☼☼☼☼☼☼☼☼ Seno, Cosseno e Tangente ☼☼☼☼☼☼☼☼☼☼'\033[m\n")

ang = float(input('  Informe o ângulo que você deseja calcular: '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('')
print(f'    O ângulo do seno é:......... {seno:.2f}\n'
      f'    O ângulo do cosseno é:...... {cosseno:.2f}\n'
      f'    E a sua tangente é:......... {tangente:.2f}'
      f'\n\n           ---- Fim do programa ----')

# --------------------------------------------------------------------------


angulo = float(input('Digite um ângulo que você deseja: '))

senO = sin(radians(angulo))

print(f'O ângulo de {angulo} tem o SENO de: {senO:.2f}')

cossenO = cos(radians(angulo))

print(f'O ângulo de {angulo} tem o COSSENO de {cossenO:.2f}')

tangentE = tan(radians(angulo))

print(f'O ângulo de {angulo} tem a TANGENTE de: {tangentE:.2f}\n\n ---- Fim do programa ----')

# --------------------------------------------------------------------------
