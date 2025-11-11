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
pessoa = {
    'nome': 'Igor',
    'sobrenome': 'Vila',
    'idade': 30

}

# Caso exista a chave o setdefault nao vai fazer nada 
pessoa.setdefault('idade', None)
print(pessoa['idade'])
# print(len(pessoa))
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())


# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave,valor)