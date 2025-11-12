"""
Metodos uteis dos dicionarios em Python 
len - quantas chaves 
keys - iteravel com as chaves 
values - Iteravel com os valores 
items - iteravel com as chaves e valors 
setdefault - adiciona valor se a chave nao existe 
copy - retorna uma copia rasa (shallow copy)
get - obtem uma chave 
pop - apaga um item com a chave especificada (del)
popitem - apaga o ultimo item adicionado 
update - atualiza um dicionario com outro 
"""
# se um dicionario tiver duas chaves iguais, o valor que vai assumir é o ultimo
p1 = {
    'nome': 'Igor',
    'sobrenome': 'Vila',
}

# print(p1.get('nome'))

# apagar chave especifica, pop()
# nome = p1.pop('nome')
# print(nome)
# print(p1)

# apaga a ultima chave 
# sobrenome = p1.popitem()
# print(sobrenome)
# print(p1)

# update atualiza as chaves e cria caso na tem a chave informada 
# p1.update({
#     'nome' : 'Novo Valor',
#     'idade': 30
# })

# outra forma de update 
# p1.update(nome='Luiz', idade=30)

#outra forma de update 
# tupla = ('nome', 'Novo valor'), ('idade', 30)
# p1.update(tupla)

# outra forma 
lista = [['nome', 'Novo Valor'],['idade', 30]]
p1.update(lista)

print(p1)