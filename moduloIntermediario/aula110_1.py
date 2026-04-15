

from itertools import groupby


alunos = [
    {'nome' : 'Igor', 'nota': 'A'},
    {'nome' : 'Luiz', 'nota': 'B'},
    {'nome' : 'João', 'nota': 'A'},
    {'nome' : 'Fabio', 'nota': 'C'},
    {'nome' : 'Lucas', 'nota': 'D'},
    {'nome' : 'Andre', 'nota': 'A'},
    {'nome' : 'Joana', 'nota': 'B'},
    {'nome' : 'Maria', 'nota': 'A'},
    {'nome' : 'Flavia', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)

# for aluno in alunos_agrupados:
#     print(aluno)

# alunos = ['a', 'a', 'a', 'b', 'c']
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    grupo_listado = sorted(list(c['nome'] for c in grupo))
    print(grupo_listado)