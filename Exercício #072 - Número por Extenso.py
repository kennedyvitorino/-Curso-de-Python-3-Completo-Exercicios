"""Exercício Python 072: Crie um programa que tenha uma dupla totalmente
preenchida com uma contagem por extenso, de zero até vinte. Seu programa
deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# Alt + 186 ║
# --------------------------------------------------------------------------

numero_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
                      'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                      'treze', 'catorze', 'quinze', 'desesseis',
                      ' dezessete', 'dezoito', ' dezenove', 'vinte')

# while True:
#     numero = (input('Digite um número entre 0 e 20: ')).strip()
#     if 0 <= numero <= 20:
#         break
#     print('Tente novamente. ', end='')
# print(f'Você digitou o número: {numero_por_extenso[numero]}')

# --------------------------------------------------------------------------
# Mesmo exercício, porem com opção de continuar

numero_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
                  'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                  'treze', 'catorze', 'quinze', 'desesseis',
                  ' dezessete', 'dezoito', ' dezenove', 'vinte')

while True:
    num = int(input('Digite um número de 0 a 20.'))
    if 0 < num > 20:
        print('Número inválido. Tente novamente.', end='')
    else:
        print(f'Você digitou {numero_extenso[num]}')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('Programa finalizado.')

# --------------------------------------------------------------------------
