"""Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome 'CAMPINA'."""

city = str(input('Em qual cidade você nasceu: ')).strip()

print(city[:7].upper() == 'CAMPINA')

# --------------------------------------------------------------------------

print('\n*----- Verificando as primeiras letras de um texto -----*\n')

cit = str(input('    Em qual cidadade você nasceu? ')).strip()  # strip() para excluir espaços antes e depois dos caracteres.

print(cit[:7].upper() == 'CAMPINA',
                         '\n\n               *--*-- Fim do programa --*--*')

# --------------------------------------------------------------------------

city = str(input('Em que cidade você nasceu? ')).strip()  # .strip() para eliminar espaços indesejados.
print(city[:7].upper() == 'CAMPINA', '\n\n Fim do exercício!')

# --------------------------------------------------------------------------

cidade = str(input('Qual o nome da cidade onde você nasceu?')).strip()
print(cidade[:7].upper() == 'CAMPINA', '\n\n Fim do exercício!')

# --------------------------------------------------------------------------
cidade = str(input('Nome da cidade: ')).strip()

print(cidade[:7].upper() == 'CAMPINA')
