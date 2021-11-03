""" Exercício Python 065: Crie um programa que leia vários
números inteiros pelo teclado. No final da execução, mostre
a média entre todos os valores e qual foi o maior e o menor
valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores. """
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# Alt + 186 ║
# --------------------------------------------------------------------------

print('\033[96m╔════════════════════════════════════╗'
      '\n║\033[97m       Menor e maior valores\033[96m        ║ \n'
      '╚════════════════════════════════════╝\n\033[m\033[97m')

resposta = 'S'
soma = quantidade = media = maior = menor = 0

while resposta in 'Ss':
    numero = int(input(' Digite um número: '))
    soma += numero  # ou sem simplificar: soma = soma + num
    quantidade += 1  # ou sem simplificar:  quant = quant + 1

    if quantidade == 1:
        maior = menor = numero  # se o usuário entrar com 1 numero apenas, será ambos o maior e menor.

else:
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

resposta = str(input(' Deseja continuar? [S/N]')).upper().strip()
media = soma / quantidade

print(f'\n Você digitou {quantidade} números e a média foi {media}\n'
      f' O maior valor foi {maior} e o menor foi {menor}.')

# --------------------------------------------------------------------------


resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num  # ou sem simplificar: soma = soma + num
    quant += 1  # ou sem simplificar:  quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
