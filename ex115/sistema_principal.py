from ex115.lib.interface0 import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])

    if resposta == 1:
        cabecalho('opção 1: ')
    elif resposta == 2:
        cabecalho('opção 2: ')
    elif resposta == 3:
        cabecalho('\033[91mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[91mERRO: Digite uma opção válida!\033[m')
        sleep(0.5)
