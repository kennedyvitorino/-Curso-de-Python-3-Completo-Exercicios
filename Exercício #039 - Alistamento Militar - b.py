from datetime import date
nome = str(input('Informe o seu nome: '))
print('''Qual é seu gênero: 
[1] Feminino
[2] Masculino''')

genero = int(input('Escolha a opção correta de acordo com a lista acima: '))
if genero ==1:
    print('Você não precisa se alistar.\nObrigado por usar o programa!')
    quit()
elif genero != 1 and genero != 2:
    print('Você usou uma opção inválida, por favor tente novamente.')
    quit()
else:
    print('Você é Homem e tem o alisamento obrigatório!')
nasci = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasci
print(f'Quem nasceu em {nasci} tem {idade} anos em {atual}')
if idade == 18:
    print('Você deve se alistar ainda este ano!')
elif idade < 18:
    print(f'Você ainda não tem a idade necessária para o alistamento,\nE conforme a sua idade será em {18 - idade} ano(s). No ano de {atual + (18 - idade)} ')
else:
    print(f'Você já se alistou, e isso foi há {idade - 18} ano(s) atrás \nNo ano de \033[1;31m{atual -(idade - 18)}')