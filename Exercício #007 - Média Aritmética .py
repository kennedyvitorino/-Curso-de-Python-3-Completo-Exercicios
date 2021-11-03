"""Exercício Python 007: Desenvolva um programa que leia as duas
notas de um aluno, calcule e mostre a sua média."""
import math

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))

media = nota1 + nota2 / 2

print(f'A primeira nota foi {nota1} \n'
      f'A segunda nota foi {nota2} \n'
      f'A média foi {media} \n'
      f'Fim do programa.')

# --------------------------------------------------------------------------

num1 = float(input('Primeira nota:'))
num2 = float(input('Segunda nota:'))
num3 = float(input('Terceira nota:'))
num4 = float(input('Quarta nota:'))
media = (num1 + num2 + num3 + num4) / 4

print(f'A sua média foi: {media}')

# --------------------------------------------------------------------------

print(f'• Crie um programa que leia as duas notas de um aluno e CALCULE e MOSTRE a MÉDIA.\n'
      f'• A seguir informe suas notas em cada DISCIPLINA!\n')

n1 = float(input('• Quanto voce tirou em PORTUGUES?'))
n2 = float(input('• Quanto tirou em  MATEMÁTICA?'))
n3 = float(input('• Quanto tirou em HISTÓRIA?'))
n4 = float(input('• Quanto tirou em GEOGRAFIA?'))
n5 = float(input('• Quanto tirou em FÍSICA?'))
n6 = float(input('• Quanto tirou em QUÍMICA?'))
n7 = float(input('• Quanto tirou em FILOSOFIA?'))

m = float((n1 + n2 + n3 + n4 + n5 + n6 + n7)/7)

print(f'\n•A sua média geral é: {m:.2f}\n•A sua MÉDIA geral é: {math.ceil(m):.2f}\n•A sua MÉDIA geral é: {math.floor(m):.2f}\n')

if m > 5.99:
    print(f'Nota de português: {n1}\nNota de matemática: {n2}\n'
          f'Nota de história: {n3}\nNota de geografia: {n4}\n'
          f'Nota de física: {n5}\nNota de química: {n6}\n'
          f'Nota de filosofia: {n7}\n')

    print('•Você foi Aprovado\nPARABÉNS!\n\n•Fim do EXERCÍCIO!')
else:
    print(f'Nota de português: {n1}\nNota de matemática: {n2}\n'
          f'Nota de história: {n3}\nNota de geografia: {n4}\n'
          f'Nota de física: {n5}\nNota de química: {n6}\n'
          f'Nota de filosofia: {n7}\n')

    print('•Você foi Reprovado\n\nnContinue se estudando!')

# --------------------------------------------------------------------------
