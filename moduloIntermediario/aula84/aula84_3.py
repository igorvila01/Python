# list comprehension em python 
# List comprehension é uma forma rapida para criar listas 
# a partir de iteraveis 

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# print(list(range(10)))

# lista = []

# for numero in range(10):
#     lista.append(numero)

# print(lista)


# posso fazer um for dentro de uma lista para ser incluido o mesmo valor que foi anteriormente 

# lista = [numero for numero in range(10)] 
# print(lista)

# # posso tambem fazer operaçoes dentro tambem 
# lista = [
#     numero * 2
#     for numero in range(10)
#     ] 
# print(lista)


# Mapeamento de dados em list comprehension 
produtos = [ 
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},

]

novos_produtos = [

    {**produto, 'preco' : produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(*novos_produtos, sep = '\n')
# p(novos_produtos)

# filtros em list comprehension 
# lista = [n for n in range(10) if n < 5 ]
# print(lista)

# o que esta na esquerda do for é mapeamento e o que esta a direita é filtro 
novos_produtos = [

    {**produto, 'preco' : produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco']) > 10

]

p(novos_produtos)
