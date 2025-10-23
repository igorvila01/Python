"""
Repetiçoes 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira 
"""

#  Loop infinito quando um codigo nao tem fim
# condicao = True

# while condicao:
#     print(1)
#     print(2)
#     print(3)


condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    
    if nome == 'sair':
        break
    else:
        print(f'Seu nome é {nome}')
print('Acabou!')

