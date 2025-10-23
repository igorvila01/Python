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

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b  # concatenar lista a mais a b
lista_a.extend(lista_b)  # Nao posso armazenar esse metodo em uma variavel, porque ele esta mexendo diretamente em uma lista 
print(lista_a)