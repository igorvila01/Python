"""
Cuidados com dados mutaveis 
= - Copiado o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
"""

# nome = 'Igor'
# noutra_variavel = nome
# nome = 'Joao'
# print(nome)
# print(noutra_variavel)

# l_a = ['Igor', 'Luiz']

# # Nunca copiar uma lista para outra variavel dessa forma, pois as 2 variaveis ira acessar a mesma informação na memoria 
# l_b = l_a
# l_a[0] = 'Qualquer coisa'
# print(l_b)


# Sempre que for copiar uma lista com valores mutaveis, utilizar o metodo copy
l_a = ['Igor', 'Luiz', 1, True, 1.2]
l_b = l_a.copy()

l_a[0] = 'Qualquer coisa'
print(l_b)
print(l_a)