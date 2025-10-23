"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo 
Conhecimentos reutilizaveis - indices e fatiamento 
Metodos uteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar  Ler  Alterar apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

# Ao mover algum item do meio de uma listas, dependendo do tanto de informaçoes que tem na lista, o codigo 
# ira ficar lento devido ele ter que ajeitar a lista 

lista.append(50)  # append adiciona itens ao final da lista e pode ser usado quantas vezes quiser 
lista.pop()   # pop remove o ultimo item de uma lista, no caso o proximo é um append, ele vai substituir o 50 da lista 
lista.append(60)   
lista.append(70) 
lista.pop(3)  # Escolher o indice que quero remover 
ultimo_valor = lista.pop()  # Gravar o ultimo valor removido na variavel
print(lista, 'Removido, ', ultimo_valor)

