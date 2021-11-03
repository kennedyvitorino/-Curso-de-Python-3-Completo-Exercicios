""" Exercício Python 008: Escreva um programa que leia um
valor em metros e o exiba convertido em centímetros e milímetros."""


print('\033[92m~' * 24)
print('  Conversor de Medidas ')
print('~' * 24, '\033[m')

metros = float(input('Conversor de METROS para:\n'
                     ' [DM] Decímetros \n'
                     ' [CM] Centímetros \n'
                     ' [MM] Milímetros \n'
                     ' [DAM] Decâmetros \n'
                     ' [HM] Hectômetros \n'
                     ' [KM] Quilômetros\n'
                     'Informe o valor em METROS para ver sua conversão: '
                     ))

decimetro = metros * 10        # Decímetros  = DM
centimetros = metros * 100     # Centímetros = CM
milimetros = metros * 1000     # Milímetros  = MM

decametro = metros / 10        # Decâmetros  = DAM
hectometro = metros / 100      # Hectômetros = HM
quilometro = metros / 1000     # Quilômetros = KM

print(f'{metros}(metros) convertidos em Decímetros (dm) equivale a {decimetro:.2f} \n'
      f'{metros}(metros) convertidos em Centímetros (cm) equivale a {centimetros:.0f} \n'
      f'{metros}(metros) convertidos em Milímetros (mm) equivale a {milimetros:.0f} \n'

      f'{metros}(metros) convertidos em Decâmetros (dam) equivale a {decametro:.2f} \n'
      f'{metros}(metros) convertidos em Hectômetros (hm) equivale a {hectometro:.2f} \n'
      f'{metros}(metros) convertidos em Quilômetros (km) equivale a {quilometro:.3f} \n\n'
      f'Fim do programa!')


# --------------------------------------------------------------------------

medida = int(input('Informe uma medida em metros: '))

milimetros = medida * 1000  # mm
centimetros = medida * 100  # cm
decimetro = medida * 10     # dm
decametro = medida / 10     # dam
hectometro = medida / 100   # hm
quilometro = medida / 1000  # km

print(f'{medida}m convertidos em centimetros equilave a {centimetros:.0f}cm \n'
      f'{medida}m convertidos em milímetros equilave a {milimetros}mm \n'
      f'{medida}m convertidos em decímetros equilave a {decimetro}dm \n'
      f'{medida}m convertidos em decâmetros equilave a {decametro:.0f}dam \n'
      f'{medida}m convertidos em hectometros equilave a {hectometro:.0f}hm \n'
      f'{medida}m convertidos em quilômetros equilave a {quilometro:.0f}km')

# --------------------------------------------------------------------------

medida = int(input('Digite uma medida em metros: '))

mm = medida * 1000   # milímetro
cm = medida * 100    # centímetro
dm = medida * 10     # decímetro
dam = medida / 10    # decâmetro
hm = medida / 100    # hectômetro
km = medida / 1000   # quilômetro

print(f'{medida}m convertidos em centimetros equilave a {cm:.0f} centímetro(s) \n'
      f'{medida}m convertidos em milímetros equilave a {mm} milímetro(s) \n'
      f'{medida}m convertidos em decímetros equilave a {dm} decímetro(s) \n'
      f'{medida}m convertidos em decâmetros equilave a {decametro:.2f} decâmetro(s) \n'
      f'{medida}m convertidos em hectometros equilave a {hectometro:.2f} hectometro(s) \n'
      f'{medida}m convertidos em quilômetros equilave a {quilometro:.3f} quilômetro(s)')

# --------------------------------------------------------------------------
