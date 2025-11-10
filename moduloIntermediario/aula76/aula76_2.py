"""Dicionarios em Python 
Dicionarios são estruturas de dados do tipo par de "Chave" e "Valor" .
Chaves podem ser consideradas como o 'Indice' que vimos na lista e podem ser de tipos imutaveis 
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionario.
Usamos as chaves - {} - ou a classe dict para criar dicionarios
Imutaveis: str, int, float, bool, tuple 
Mutaveis: dict, list

"""
# Forma mais comum utilizada
pessoa = {}

# armazenar uma chave em uma variavel posso torna-la dinamica 
chave = 'nome'

# Criação de chave e valor para dicionario 
pessoa[chave] = 'Igor'
pessoa['sobrenome'] = 'Vila'


print(pessoa[chave])

# alterando o valor de uma chave 
pessoa[chave] = 'Maria'

# deletar uma chave
del pessoa['sobrenome']

print(pessoa)

# verificar se uma chave existe para nao dar erro
if pessoa.get('sobrenome') is None:
    print('Nao Existe')
else:
    print(pessoa['sobrenome'])


