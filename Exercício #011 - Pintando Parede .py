"""Exercício Python 011: Faça um programa que leia a largura
e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada
litro de tinta pinta uma área de 2 metros quadrados."""

# --------------------------------------------------------------------------

print('-=' * 17)
print(' Calculando a área de uma parede')
print('-=' * 17)

larg = float(input('Largura:....'))
altu = float(input('Altura:.....'))

area = larg * altu
tinta = area / 2

print(f'As dimensões da parede são: \n'
      f'Largura:... {larg:.2f} \n'
      f'Altura:.... {altu:.2f} \n'
      f'Área:...... {area:.2f}m² \n\n'
      f'Para pintar uma parede com a área de {area}m², será necessário {tinta} litros de tinta. \n'
      f'Fim do programa!'
      )

# --------------------------------------------------------------------------

print('*---------- CALCULANDO A ÁREA DE UMA PAREDE ----------*\n')

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura
tinta = area / 2

print(f'\nA dimensão da sua parede é de {largura}x{altura} e sua área é de {area}m²\n')
print(f'Para pintar esta parede será necessário {tinta} litro(s) de tinta.\n')
print('        *---------- Fim do programa ----------*')

# --------------------------------------------------------------------------
