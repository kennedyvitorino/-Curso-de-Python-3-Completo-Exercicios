"""Adicione o módulo moeda.py criado nos desafios anteriores,
uma função chamada resumo(), que mostre na tela algumas
informações geradas pelas funções que já
temos no módulo criado até aqui.."""
from ex110 import moeda_3

for c in range(0, 5):

    p = float(input('Digite o preço: R$'))
    moeda_3.resumo(p)


