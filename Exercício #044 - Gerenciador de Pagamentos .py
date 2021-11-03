"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚

valor_produto = float(input('Quanto custou sua compra total: R$'))

option = int(input("""Formas de pagamento
[1] À vista no dinheiro ou cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2 vezes no cartão: preço normal
[4] Em 3 vezes ou mais no cartão: 20% de juros
Por favor, escolha uma das formas de pagamento acima: """))

if option == 1:
    desconto10 = valor_produto - (valor_produto * 10) / 100
    print(f'\nSua compra deu um total de R${valor_produto:.2f}, com 10% de desconto ficou R${desconto10:.2f}')
elif option == 2:
    desconto5 = valor_produto - (valor_produto * 5) / 100
    print(f'\nSua compra deu um total de R${valor_produto:.2f}, com 5% de desconto ficou R${desconto5:.2f}')
elif option == 3:
    parcela = valor_produto / 2
    print(f'\nSua compra deu um total de R${valor_produto:.2f} em duas vezes de R${parcela:.2f} sem juros.')
if option > 4:
    print('\nForma de pagamento inválida! \n'
          'Retorne ao início do progroma para começar novamente.')

elif option == 4:
    juros20 = valor_produto + (valor_produto * 20 ) / 100
    parcelas = int(input('\nem quantas vezes você deseja parcelar? '))
    parcela = valor_produto / parcelas
    print(f'Sua compra deu um total de R${valor_produto:.2f} \n'
          f'Parcelada em {parcelas} vezes de R${parcela:.2f}')

# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m               Gerenciando pagamentos'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\n')

print("            \033[1;94m╔═══════════════════════════╗\n"
      "            ║\033[m      \033[1;97mGordo's Store™\033[m       \033[1;94m║\n"
      "            ╚═══════════════════════════╝\033[m")

preco = float(input('\n\033[97m  Qual o preço total das duas compras: R$'))

opcao = int(input("""\n  Formas de pagamento disponíveis:\n
  [1] Àvista no dinheiro ou cheque
  [2] Àvista no cartão de crédito
  [3] 2x vezes no cartão de crédito
  [4] 4x ou mais no cartão de crétido\n
  Escolha a forma de pagamento disponível no sistema: """))

if opcao == 1:
    totaL = preco - (preco * 10 / 100)
    print(f'\n O valor da sua compra com nosso desconto de 10% é: {totaL:.2f}R$\n')

elif opcao == 2:
    totaL = preco - (preco * 5 / 100)
    print(f'\n  O valor da sua compra com nosso desconto de 5% é: {totaL:.2f}R$\n')

elif opcao == 3:
    totaL = preco
    parcela = totaL / 2
    print(f'\n  Suas compras de {totaL:.2f}R$, será parcelada em 2x (duas vezes)\n'
          f'  sem juros de {parcela:.2f}R$ mensais.')

if opcao > 4:
    print('  Esta forma de pagamento não existe no nosso sistema.\n'
          '  Por favor, volte para o início e escolha outra forma de pagamento!\n')

elif opcao == 4:
    totaL = preco + (preco * 20 / 100)
    total_par = int(input('\n  Em quantas vezes você deseja parcelar suas compras? '))
    parcela = totaL / total_par
    print(f'\n  Sua compra será parcelada em {total_par}x de {parcela:.2f}R$ com 20% de juros.')

print("         \033[1;94m╔═══════════════════════════════════╗\n"
      "         ║\033[m   \033[1;97mAgradecemos a sua preferência\033[m   \033[1;94m║\n"
      "         ╚═══════════════════════════════════╝\033[m")



# --------------------------------------------------------------------------


store1 = ' Lojinha do Gordo™ '
print(f'\033[1;31m{store1:=^40}\033[m')
price = float(input('Preço das suas compras: R$'))
print(f'''Formas de pagamento disponíveis 
[1] À vista no dinheiro ou cheque
[2] À vista no cartão de crédito
[3] 2x no cartão de crédito
[4] 4x ou mais no cartão de crédito''')
option = int(input('\nEscolha como deseja pagar pela sua compra: '))
if option == 1:
    total = price - (price * 10 / 100)
    print(f'\nO valor da sua compra com 10% de desconto é de: R${total:.2f}.')
elif option == 2:
    total = price - (price * 5 / 100)
    print(f'\nO valor da sua compra com 5% de desconto é de: R${total:.2f}')
elif option == 3:
    total = price
    quota = total / 2
    print(f'\nSua compra de RS{total:.2f} será parcelada em \033[1m2x (duas vezes)\033[m sem juros de R${quota:.2f}')
elif option == 4:
    total = price + (price * 20 / 100)
    total_quota = int(input(f'\nEm quantas vezes você deseja parcelar sua compra? '))
    quota = total / total_quota
    print(f'\nSua compra será parcelada em \033[1m{total_quota}x\033[m de R${quota:.2f} com \033[1m20%\033[m de juros.')
