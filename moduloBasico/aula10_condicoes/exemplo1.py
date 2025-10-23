"""
Condiçoes if, elif, e else - aula 4

- Hierarquia utilizamos 4 espaços
- Colocar 2 pontos apos cada condição
"""

if False:
    print('Verdadeiro.')
    print('teste teste2')
elif True:
    print('Agora é verdadeiro')
    nome = input('Qual o seu nome? ')

    print(f'Seu nome é {nome}')
elif False:
    print('Mais uma verdadeira')
    print(22+22)
else:
    print('Nao é verdadeiro')
    print('ola')
