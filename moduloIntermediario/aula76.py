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
pessoa = {
    'nome': 'Igor',
    'sobrenome': 'Vila',
    'idade' : 30,
    'altura' : 1.87,
    'enderecos' : [
        {'rua': 'tal', 'numero': 123},
        {'rua': 'taltal', 'numero': 1234},
        ]
}

# metodo menos utilizado 
# pessoa1 = dict(nome= 'Igor Vila', sobrenome = 'Luiz')

print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])