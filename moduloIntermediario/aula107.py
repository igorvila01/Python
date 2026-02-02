# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# zip_longest para zip da maior lista, lembrando que se os indices nao for iguais, ele preenchera com none 
from itertools import zip_longest

def zipper(lista1, lista2):
    lista_menor = min(len(lista1), len(lista2))
    # resultado = []
    # for i in range(lista_menor):
    #     add = lista1[i],lista2[i]
    #     resultado.append(add)    
    return [(lista1[i],lista2[i]) for i in range(lista_menor)]

cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']

print(zipper(cidade, estado))

print()
print()

# outra forma de resolver esse exercicio 
print(list(zip(cidade,estado)))


print()
print()

# fillvalue para definir um valor padrao para none 
print(list(zip_longest(cidade, estado, fillvalue='<<Vazio>>')))