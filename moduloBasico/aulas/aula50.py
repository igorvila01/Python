"""
for in com listas 
Exiba os indices da lista
0 Maria
1 Helena
2 Luiz
"""

# Minha resolução
# lista = ['Maria', 'Helena', 'Luiz']
# contador = 0

# for nome in lista:
#     print(f'{contador} {nome} {type(nome)}')
#     contador +=1



lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    
    