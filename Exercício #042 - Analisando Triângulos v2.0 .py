"""Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

reta1 = int(input('Reta 1: '))
reta2 = int(input('Reta 2: '))
reta3 = int(input('Reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Podemos formar um triângulo')
    if reta1 == reta2 == reta3:
        print('Podemos formar um triângulo Equilátero \n'
              '(todos os lados iguais).')
    elif reta1 != reta2 != reta3:
        print('Podemos formar um triângulo Escaleno! \n'
              '(todos os lados diferentes).')
    else:
        print('Podemos formar um triângulo Isósceles! \n'
              '(dois lados iguais e um diferente).')
else:
    print('Com esses ângulos não podemos formar um triângulo!')

# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 22,
      '\n\033[97m                  Análise de triângulos v2.0'
      )
print('\033[1;94m-=-\033[m' * 22)

reta1 = float(input('\n\033[97m Informe o primeiro segmento:...'))
reta2 = float(input(' Informe o segundo segmento:....'))
reta3 = float(input(' Informe o terceiro segmento:...'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\n Os segmentos informados podem formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('equilátero!\n Triângulo com todos os lados iguais.\n')

    elif reta1 != reta2 != reta3 != reta1:
        print('escaleno!\n Triângulo com todos os lados desiguais.\n')

    else:
        print('isósceles!\n Triângulo de dois lados iguais.\n')

else:
    print(' Os segmentos informados não podem formar um triângulo.\n')


print('\033[1;94m-=-\033[m' * 22,
      '\n\033[97m                         Fim do programa'
      )
print('\033[1;94m-=-\033[m' * 22)

# --------------------------------------------------------------------------

re1 = float(input('Digite o 1º segmento: '))
re2 = float(input('Digite o 2º segmento: '))
re3 = float(input('Digite o 3º segmento: '))
if re1 < re2 + re3 and re2 < re1 + re3 and re3 < re1 + re2:
    print('Os segmentos informados podem formar um \033[1;35mTriângulo ', end='')
    if re1 == re2 == re3:
        print('Equilátero!')
    elif re1 != re2 != re3 != re1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Os segmentos informados não podem formar um \033[1;4;31mTriângulo\033[m.')

# --------------------------------------------------------------------------
