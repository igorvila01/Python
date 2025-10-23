"""
Flag (bandeira - Marcar um local)
none = Nao Valor
is e is not = é ou nao é (tipo, valor, identidade)
id = Identidade

"""

v1 = 'a'
v2 = 'b'

# Id mostra a identidade na memoria 
print(id(v1))
print(id(v2))

# -----------------------------------------------
condicao = True

# criar a variavel fora pra nao ter que cria-la novamente dentro do else 
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Nao Faça algo')

if passou_no_if is None:
    print('Passou no if')
else:
    print('Nao passou no if')

