"""Escreva um programa que leia o nome de uma
pessoa e diga se ela tem "SILVA" no nome."""

# --------------------------------------------------------------------------

nome = str(input('Digite seu nome: ')).strip()

print(f'No seu nome tem Davyd? {"davyd" in nome.lower()} \n'
      f'No seu nome tem Silva? {"silva" in nome.lower()} \n'
      f'Fim do programa')

# --------------------------------------------------------------------------

print("\n'*---- Procurando uma STRING dentro de outra ----*'\n\n")

nome = str(input('    Qual é o seu nome completo? ')).strip()

print(f"\n    No seu nome tem: Davyd?..... {'davyd' in nome.lower()}\n"
      f"    No seu nome tem: Kennedy?... {'kennedy' in nome.lower()}\n"
      f"    No seu nome tem: Vitorino?... {'vitorino' in nome.lower()}\n"
      f"    No seu nome tem: silva?..... {'silva' in nome.lower()}\n"
      f"    No seu nome tem: Dantas?.... {'dantas' in nome.lower()}\n\n"
      f"     '***** Fim do programa *****'")

# --------------------------------------------------------------------------

sujeito = str(input('Qual é o seu nome completo? ')).strip()
print(f'Seu nome tem Silva? {"silva" in sujeito.lower()}')  # usar "aspas duplas" quando precisar por dentro de CHAVES.
print(f'Seu nome tem Silva? {"silva" in sujeito.lower()}')
print(f'Seu nome tem Kennedy? {"kennedy" in sujeito.lower()}\n\n Fim do exercício!')
