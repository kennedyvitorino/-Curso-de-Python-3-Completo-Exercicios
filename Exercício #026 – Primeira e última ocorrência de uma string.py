"""Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra 'A'.
Em que posição ela aparece pela primeira vez.
EM que posição ela aparece pela última vez."""

frase = str(input('Digite uma frase qualquer: ')).upper().strip()

print(f'A letra a aparece {frase.count("A ")} vezes na frase \n'
      f'A primeira ocorrencia da letra "A" foi na posição: {frase.find("A") + 1} \n'
      f'A última ocorrencia da letra "A" foi na posiçlão: {frase.rfind("A") + 1} \n'
      f'Fim do programa')

# --------------------------------------------------------------------------

print("\n'*----* Primeira e última ocorrência de uma string *----*'\n\n")

frase0 = str(input('Digite uma frase: ')).upper().strip()

print(
    f'A letra *A* aparece {frase0.count("A")} vezes na frase\n'
    f'A primeira letra *A* apareceu na posição {frase0.find("A") + 1}\n'
    f'A última letra *A* apareceu na posição {frase0.rfind("A") + 1}'
    )

# --------------------------------------------------------------------------

frase = str(input('Digite uma frase:')).upper().strip()

print(
    f'A letra |A| aparece {frase.count("A")} vezes na frase\nA primeira letra |A| apareceu na posição {frase.find("A") + 1}\nA última letra |A| apareceu na posição {frase.rfind("A") + 1}\n\n Fim do exercício!')
