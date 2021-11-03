""" Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário
se ele quer mostrar mais alguns termos. O programa encerrará quando ele
disser que quer mostrar 0 termos. """
from time import sleep
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# Alt + 186 ║
# --------------------------------------------------------------------------

print('\033[92m╔════════════════════════════════════╗'
      '\n║   \033[97mSuper progressão aritmética v2.0 \033[92m║ \n'
      '║         \033[97mTermos de uma PA           \033[92m║\n'            
      '╚════════════════════════════════════╝\n\033[m\033[97m')

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro_termo
cont = 1  # contador
total = 0  # total de termos
mais = 10  # quantos termos ler e mostrar na tela

while mais != 0:  # enquanto o mais for diferente de 0
    total += mais

    while cont <= total:
        print(f'\033[1;91m{termo} → ', end='\033[m')
        sleep(0.20)
        termo += razao
        cont += 1

    print('\n\033[97mPause')

    mais = int(input('Quantos termos a mais você deseja mostrar? '))

print(f'Progressão finalizada com o total de {total} termos mostrados.\n')

print('\033[92m╔════════════════════════════════════╗'
      '\n║          \033[97m Fim do programa \033[92m         ║ \n'           
      '╚════════════════════════════════════╝\n\n\033[m\033[97m')

# --------------------------------------------------------------------------


print('\033[1;35m-=\033[m' * 10)
print('\033[31mTermos de uma PA!\033[m')
print('\033[1;35m-=\033[m' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1  # contador
total = 0  # total de termos
mais = 10  # quantos termos ler e mostrar
while mais != 0:  # enquanto o mais for diferente de 0
    total = total + mais
    while cont <= total:  # enquanto o contador for menor ou igual ao total
        print(f'\033[1;34m{termo} → ', end='\033[m')
        sleep(0.25)
        termo += razao
        cont += 1
    print('Pause')
    mais = int(input('Quantos termos você deseja mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
