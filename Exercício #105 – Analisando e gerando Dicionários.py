"""Exercício Python 105: Faça um programa que tenha uma função
notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)"""


def notas(* num, sit=False):
    """\033[91m
    +------+----------+----------+----------+----------+------+
    | -> Função para analisar notas e                         |
    | situações de vários alunos.                             |
    | :param num: um ou mais notas dos alunos (aceita várias).|
    | :param sit: valor opcional, indicando se                |
    | deve ou não adicionar a situação.                       |
    | :return: dicionário com várias                          |
    | informações sobre a situação da turma.                  |
    +------+----------+----------+----------+----------+------+

    \033[m"""

    r_dict = dict()
    r_dict['Total'] = len(num)
    r_dict['Maior'] = max(num)
    r_dict['Menor'] = min(num)
    r_dict['Média'] = sum(num) / len(num)

    if sit:
        if r_dict['Média'] >= 7:
            r_dict['Situação'] = 'BOA!'
        elif r_dict['Média']:
            r_dict['Situação'] = 'RAZOÁVEL!'
        else:
            r_dict['Situação'] = 'RUIM!'

    return r_dict


# Programa Principal
resposta = notas(5.5, 2.5, 9, 8.5, sit=True)

print(resposta)
help(notas)
