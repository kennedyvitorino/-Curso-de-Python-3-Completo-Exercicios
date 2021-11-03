tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

print(sorted(tupla))

num = [3, 6, 4, 1]

for n1, n2 in enumerate(num):
    print(n1 + n2)

paises = ('brasil', 'uruguai','japao','eua')

print(paises[0], paises[-1])

val = list(range(1, 5))

print(val)

letras = ('J', 'X', 'M', 'O', 'A', 'K')

print(letras.index('A'))

num = [6, 2, 1, 4, 3]

num.sort(reverse=True)
print(num)

num = [2, 8, 4, 7]
num.pop()
num.insert(1, 3)
num.append(6)
print(num)
