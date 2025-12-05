# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir(lista):
    for item in lista:
        print(item)

# Exemplo de função comum para ordenar por nome
# def orderna(item):    
#     return item['nome']

# lista.sort(key=orderna)

# for item in lista:
#     print(item)

# Exemplo de ordenação utilizando função lambda 
# utilizando o sort, vai alterar realmente a order da lista 
# lista.sort(key=lambda item: item['nome'])

# Para fazer uma copia rasa da lista sem altera-la, preciso criar uma variavel e utilizar o sorted 
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

print('Ordenando por nome: ')
exibir(l1)
print('\nOrdenando por Sobrenome:')
exibir(l2)