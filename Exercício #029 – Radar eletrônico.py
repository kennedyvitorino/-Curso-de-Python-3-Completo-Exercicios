"""Escreva um programa que leia a velocidade de um carro.
Se ele tá a 80Km/h, mostre uma mensagem
dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite."""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

# vai ser subtraido os 80 e o excedente será multiplicado por 7
# (multa = R$7.00 por km que o carro passou do limite)

velocidade = float(input('Em qual velocidade você passou no radar: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    limite = velocidade - 80

    print(f'Você passou no radar a {velocidade}Km por hora. \n'
          f'O limite de velocidade é de 80km e você excedeu em {limite}Km \n'
          f'Você foi multado em R${multa:.2f}')
else:
    print(f'Você passou no radar a {velocidade}Km por hora. \n'
          f'Tenha um bom dia')

# --------------------------------------------------------------------------

print('\n\n \033[1;97m╔═══════════════\033[m \033[1;94mRADAR ELETRONICO\033[m \033[1;97m═══════════════╗\033[m\n')

veloc = float(input('      Qual é a velocidade atual do seu carro? '))

if veloc > 80:
    # vai ser subtraido os 80 e o excedente será multiplicado por 7
    # (multa = R$7.00 por km que o carro passou do limite)
    multa = (veloc - 80) * 7
    limite_km = veloc - 80

    print(f'\n      Você passou no radar a {veloc}Km por hora.\n'
          f'      O limite permitido é de 80Km por hora.\n'
          f'      Você passou excedeu em {limite_km}km\n'
          f'      O valor da multa é de R${multa}\n')

else:
    print(f'\n      Você passou no radar a {veloc}Km por hora.\n'
          f'      Tenha um bom dia.\n')

print('  \033[1;97m╩═══════════════\033[m \033[1;94mFIM DO PROGRAMA\033[m \033[1;97m═══════════════╩\033[m ')
# --------------------------------------------------------------------------


velocidade = float(input('Qual é a velocidade atual do carro? '))
cores = {'limpa': '\033[m',
         'ver_negrito': '\033[1;31m',
         'verm': '\033[31m',
         'verde': '\033[32m',
         'pretoebranco': '\033[7;30m'
         }

if velocidade > 80:
    print(f'{cores["ver_negrito"]}|Multado!|{cores["limpa"]} Você excedeu o limite permitdo que é de {cores["verde"]}80Km/h{cores["limpa"]}')
    multa = (velocidade - 80) * 7  # vai ser subtraindo os 80 e o excedente será multiplicado por 7.
    print(f'O Valor da multa é de: {cores["ver_negrito"]}{multa:.2f}R${cores["limpa"]}')
else:
    print(f'\n{cores["pretoebranco"]}Tenha um bom dia!{cores["limpa"]}\n{cores["pretoebranco"]}Dirija com cuidado!{cores["limpa"]}')
