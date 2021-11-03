"""Exercício Python 006: Crie um algoritmo que leia um
número e mostre o seu dobro, triplo e raiz quadrada."""

num = int(input('Digite um número para ver o seu DOBRO, TRIPLO, RAIZ QUADRADA e RAIZ CÚBICA: '))

dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** (1 / 2)
raiz_cubica = num ** (1/3)

print(f'O dobro de {num} é {dobro} \n'
      f'O triplo de {num} é {triplo} \n'
      f'A raiz quadrada de {num} é {raiz_quadrada} \n'
      f'A raiz cúbica de {num} é {raiz_cubica} \n'
      f'Fim do programa.')

# --------------------------------------------------------------------------

numero = int(input(" Informe um número:"))

dobro = numero * 2
triplo = numero * 3
raizQ = numero ** (1 / 2)

print(f'O dobro de {numero} é: {dobro}, o seu tiplo é {triplo} e sua raiz quadrada é: {raizQ:.0f}')

# --------------------------------------------------------------------------

num = int(input('Informe um valor :'))
print(f'O dobro de {num} é {numero * 2}, o triplo é {numero * 3} e a sua raizQ é {numero ** (1 / 2):.0f}')

# --------------------------------------------------------------------------

n1 = int(input('  • Diga um valor para que seja mostrado o resultado: '))

d = n1 * 2
t = n1 * 3
r = n1 ** (1 / 2)

print(f'O dobro de {n1} é {d}\nO TRIPLO de {n1} é {t}\nE a sua RAIZ² é {r} ou {r:.2f}')

# --------------------------------------------------------------------------

n1 = int(input('  Informe um valor para que seja mostrado o Resultado: '))

d = n1 * 2
t = n1 * 3
r = n1 ** (1 / 2)  # calcular a raizQ de um número é o mesmo que criar a potencia dele por (1/2)

print(f'  O Dobro de {n1} é: {d}\n  O Triplo de {n1} é {t}\n  E sua Raiz² é: {r:.0f} ou {r:.5f}')

# --------------------------------------------------------------------------
