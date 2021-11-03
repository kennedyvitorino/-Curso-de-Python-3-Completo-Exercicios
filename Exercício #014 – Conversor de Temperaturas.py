"""Escreva um prorama que converta a temperatura
digitada em ºC e converta para ºF.
Multiplicamos a temperatura em ºC por 1,8 e somamos 32 ao resultado.
Subtraímos a temperatura em ºF por 32 e dividimos o resultado por 1,8."""

# --------------------------------------------------------------------------

celsius = float(input('Temperatura em ºC: '))
fahrenheit = float(input('Temperatura em ºF:'))

grausF = (celsius * 1.8) + 32
grausC = (fahrenheit - 32) / 1.8

print(f'{celsius}º celsius convertidos para farenheit é {grausF} \n'
      f'{fahrenheit}º farenheit convertidos para celsius é {grausC:.2f} \n'
      f'Fim do programa!')

# --------------------------------------------------------------------------

c = float(input('Informe  a Temperarua em ºC: '))
f = ((9 * c) / 5) + 32
print(f'  •A temperatura de {c}ºC (Graus Celsius) corresponde a {f}ºF (Fahrenheit)\n\n      •Fim do exercício. Boa cara!')

# --------------------------------------------------------------------------

grauC = float(input('Temperatura em Celsius: '))
grauF = float(input('Temperatura em Fahrenheit: '))

fahrenheit = (grauC * 1.8) + 32  # Multiplicamos a temperatura em ºC por 1,8 e somamos 32 ao resultado.
celsius = (grauF - 32) / 1.8  # Subtraímos a temperatura em ºF por 32 e dividimos o resultado por 1,8.

print(f'{grauC}ºC (Celsius) é equivalente a {fahrenheit}ºF (Fahrenheit) \n'
      f'{grauF}ºF (Fahrenheit) é equilavente a {celsius}ºC (Celsius).')

# --------------------------------------------------------------------------
