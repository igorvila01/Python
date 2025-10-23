"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo 
Conhecimentos reutilizaveis - indices e fatiamento 
Metodos uteis: 
    append - Adiciona um item ao final  
    insert - Adiciona um item ao indice escolhido
    pop - Remove do final ou do indice escolhido
    del - Apaga um indice 
    clear - Limpa a lista
    extend - estende a lista
    + - Concatena a lista
Create Read Update Delete
Criar  Ler  Alterar apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
lista.append('Igor')
nome = lista.pop()
lista.append(1233)
del lista[-1]

# primeiro escolha o indice e depois separe por virgula o valor que quer inserir
# Erro comum cometido é adicionar um indice maior que a lista, que no caso vai inserir no ultimo indice, mas na hora de acessar esse indice vai retornar que nao existe 
lista.insert(0, 5)  
print(lista)
