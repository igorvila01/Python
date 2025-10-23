"""
Lista de listas e seus indices 
"""
salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Igor', 'Luiz', 'João', (0,10,20,30,40)]
]

# como acessar os indices de uma lista dentro de outras listas 
print(salas[1][0])
print(salas[0][1])
print(salas[2][2])

# para acessar a tupla dentro de outra lista, coloco adiciono ou tro indice 
print(salas[2][3][3])


for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
