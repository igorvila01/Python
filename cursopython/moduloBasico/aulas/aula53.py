"""
enumerate - enumera iteraveis (indices)
"""

lista = ['Maria', 'Helena', 'Igor']
lista.append('João')

# se quiser usar o enumerator em um for, é aconselhado colocar direto ao inves de uma variavel 
# Porque a variavel é esgotada assim que termina o for, ficando dificil de utilizar 
# lista_enumerada = enumerate(lista)

for item in enumerate(lista):
    indice, nome = item
    print(indice,nome)


# lista = ['Maria', 'Helena', 'Igor']
# lista.append('João')

# lista_enumerada = list(enumerate(lista))

# print(lista_enumerada)