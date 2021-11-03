"""Desenvolva um programa que leia o comprimento
de três retas e diga ao usuários se elas podem ou
não formar um triângulo."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

reta1 = float(input('Segmento 1: '))
reta2 = float(input('Segmento 2: '))
reta3 = float(input('Segmento 3: '))

if reta1 < reta2 + reta3 \
        and reta2 < reta1 + reta3 \
        and reta3 < reta1 + reta2:
    print(f'Os segmentos: {reta1}, {reta2} e {reta3} podem formar um triângulo!')
else:
    print(f'Os segmentos: {reta1}, {reta2} e {reta3} não podem formar um triângulo!')

# --------------------------------------------------------------------------

print('\n\033[1;96m╔════════════════\033[m \033[1;91mAnalisando Triângulos\033[m \033[1;96m════════════════╗\033[m\n')


r1 = float(input('   \033[97mPrimeiro segmento:... '))
r2 = float(input('   Segundo segmento:.... '))
r3 = float(input('   Terceiro segmento:... '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    print(f'\n   Os segmentos sao:\n\n'
          f'   Primeiro segmento... {r1}\n'
          f'   Segundo segmento.... {r2}\n'
          f'   Terceiro segmento... {r3}\n\n'
          f'   Com estes ângulos é possivel formar um triângulo.')

print('\n\033[1;96m╚═══════════════════\033[m \033[1;91mFIM DO PROGRAMA\033[m \033[1;96m═══════════════════╝\033[m')

# --------------------------------------------------------------------------


print('\033[1;34m-=-\033[m' * 10)
print('Analizando Triângulos!')
print('\033[1;34m-=-\033[m' * 10)

reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f'Os segmentos: \033[1;34m{reta1}\033[m, \033[1;34m{reta2}\033[m e \033[1;34m{reta3}\033[m podem formar um TRIÂNGULO!')
else:
    print(f'Os segmentos: \033[1;31m{reta1}\033[m, \033[1;31m{reta2}\033[m e \033[1;31m{reta3}\033[m não podem formar um TRIÂNGULO!')
