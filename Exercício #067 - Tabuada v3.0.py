"""Exercício Python 067: Faça um programa que mostre
a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for negativo."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# Alt + 186 ║
# --------------------------------------------------------------------------

print('\033[96m╔════════════════════════════════╗'
      '\n║\033[1;97m         Tabuada v3.0\033[96m           ║\n'
      '╚════════════════════════════════╝\n\033[m\033[97m')

while True:
    numero = int(input(' Você quer a tabuada de qual número? '))
    print('\033[1;35m▼⌂\033[m' * 11)
    if numero < 0:
        break

    for contador in range(1, 11):
        print(f' {numero} x {contador} é igual a {numero * contador}')
    print('\033[1;35m▼⌂\033[m' * 11)
print('\033[96m╔════════════════════════════════╗'
      '\n║\033[1;97m        Fim do programa\033[96m         ║\n'
      '╚════════════════════════════════╝\n\033[m\033[97m')

# --------------------------------------------------------------------------


# while True:
#     n = int(input('Você quer a tabuada de qual número? '))
#     print('\033[1;34m-\033[m' * 30)
#     if n < 0:
#         break
#     for c in range(1, 11):
#         print(f'{n} *{c:2} é igual a: {n * c}')
#     print('\033[1;34m-\033[m' * 30)
# print('Programa encerrado, volte sempre.')

while True:
    n = int(input('Digite um valor para ver a sua tabuada: '))
    print('\033[1;35m▼⌂\033[m' * 11)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} é igual a {n * c}')
    print('\033[1;35m▼⌂\033[m' * 11)
print('Fim do programa.')
