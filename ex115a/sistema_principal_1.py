from ex115a.lib.interface1 import *
from ex115a.lib.arquivo0 import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])

    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('Opção 2: ')
    elif resposta == 3:
        cabecalho('\033[91mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[91mERRO: Digite uma opção válida!\033[m')
        sleep(0.5)
