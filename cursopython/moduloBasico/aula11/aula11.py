"""
Metodo len só funciona com strings e floats
"""

usuario = input('Digite seu usuario: ')

# Função len faz a contagem de caracteres ja é inteiro
qtd_caracteres = len(usuario)

# print(usuario, qtd_caracteres, type(qtd_caracteres))
if qtd_caracteres < 6:
    print('Voce precisa digitar pelo menos 6 caracteres')
else:
    print('Voce foi cadastrado no sistema.')
