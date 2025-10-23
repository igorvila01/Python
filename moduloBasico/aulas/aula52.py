"""
Tipo Tupla - Uma lista imutavel 
"""

# para declarar uma tupla é só nao colocar os colchetes ou parenteses 
# nomes = 'Maria', 'Helena', 'Luiz'

# print(nomes[-1])
# print(nomes)



nomes = ['Maria', 'Helena', 'Luiz']
# converter uma lista para tupla
nomes = tuple(nomes)
# converter tupla para lista 
nomes = list(nomes)


print(nomes[-1])
print(nomes)