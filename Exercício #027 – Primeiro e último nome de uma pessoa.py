"""Faça um programa que leia o nome completo de uma pessoa.
 mostrando em seguida o primeiro e o último nome separadamente."""

nome = str(input('Digite seu nome')).strip()

lista_N = nome.split()  # transforma a variável NOME em lista

print(f'O seu primeiro nome é {lista_N[0]} \n'
      f'O seu último nome é {lista_N[len(lista_N) - 1]}')

# --------------------------------------------------------------------------

print("\n       #---- Primeiro e último nome de uma pessoa ----#\n")

name = str(input('          Informe o seu nome completo: ')).strip()

name1 = name.split()

print(f'\n {name1}         É um prazer ter conhecer, {name}!\n'
      f'          Seu primeiro nome é... {name1[0]}\n'
      f'          Seu último nome é..... {name1[len(name1) - 1]}\n\n'
      f'        #_____ Fim do programa ____#')

# --------------------------------------------------------------------------


nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'\nÉ um prazer te conhecer, {nome}!\nSeu primeiro nome é: {n[0]}\nSeu último nome é: {n[len(n) - 1]}')
# print('Seu ultimo nome é{}'.format(n[len(n) - 1])) #usando formatação antiga.

# --------------------------------------------------------------------------
