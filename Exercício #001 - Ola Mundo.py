"""Faça um programa que leia o nome de uma pessoa
e mostre uma mensagem de boas-vindas."""
# print('Olá, mundo!')
#
# name = str(input('Digite seu nome: '))
# print(f"Olá {name}, Seja muito bem vindo ao » Curso em Vídeo «")
# Class
# Syntaxe


class Pessoa:
    def __init__(self, nome=None, msg=None):
        self.msg = msg
        self.nome = nome

    def mensagem(self):
        self.nome = input('Qual é o seu nome? ')
        print(f'Olá, {self.nome}! \nSeja bem vindo ao curso')


saida = Pessoa()
saida.mensagem()
