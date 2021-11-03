"""Crie um código em Python que teste
se o site pudim está acessível pelo computador usado.
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')

except urllib.error.URLError:
    print('O site PUDIM não está acessivel no momento!')

else:
    print('Consegui acessar o site PUDIM com sucesso!')
    print(f'\033[91m{site.read()}\033[m')
    