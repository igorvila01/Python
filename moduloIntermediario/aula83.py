# Empacotamento e desempacotamento de dicionarios
a, b = 1,2
a, b = b, a

pessoa = {
    'nome': 'Igor',
    'sobrenome': 'Vila',
}

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Nao Nomeados: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# caso passe um argumento nao nomeado, vai ficar gravado somente em args
# mostro_argumentos_nomeados(nome = 'Igor', qlq = 123)

# mostro_argumentos_nomeados(**pessoa_completa)

configuracao = {
    'arg1' : 1,
    'arg2' : 2,
    'arg3' : 3,
    'arg4' : 4,
}

mostro_argumentos_nomeados(**configuracao)
