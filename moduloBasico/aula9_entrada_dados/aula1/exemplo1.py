"""
Entrada de dados
"""
"""
nome = input('Qual o seu nome? ')  # input sempre retorna string
print(f'O usuario digitou {nome} e o tipo da variavel é '
      f'{type(nome)}')
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
ano_nascimento = 2025-int(idade)

print(f'\n{nome} tem {idade} anos. '
      f'\n{nome} nasceu em {ano_nascimento}')