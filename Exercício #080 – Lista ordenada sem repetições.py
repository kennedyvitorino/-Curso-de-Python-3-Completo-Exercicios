"""Exercício Python 080: Crie um programa onde o usuário
possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela."""
# --------------------------------------------------------------------------

lista = []

for contador in range(0, 5):
    num = int(input('Informe um valor: '))
    if contador == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        position = 0
        while position < len(lista):
            if num <= lista[position]:
                lista.insert(position, num)
                print(f'Adicionado na posição {position} da lista...')
                break
            position += 1

print('-=' * 27)
print(f'Os valores digitados em ordem foram {lista}')

# --------------------------------------------------------------------------

Lista = []

for contador in range(0, 5):
    numeros = int(input('Digite um valor: '))
    if contador == 0 or numeros > Lista[-1]:
        Lista.append(numeros)
        print('Adicionado ao final da lista.')
    else:
        position = 0
        while position < len(Lista):
            if numeros <= Lista[position]:
                Lista.insert(position, numeros)
                print(f'Adicionado na posição {position}')
                break
            position =+ 1

print('=-' * 27)
print(f'Os valores digitados em ordem fora, {Lista}')
