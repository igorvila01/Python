nome = 'Igor Vila'
idade = 30
altura = 1.87
e_maior = idade > 18
# data_1 = false
# data_atual = 2025
peso = 98
imc = peso / (altura**2)


print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
"""
Forma mais utilizada para concatenar utilizar a letra f antes das aspas 
separar por chaves as variaveis 

para mostrar somente 2 casas decimais colocar 2 pontos ponto 2f 
"""
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

# Outra forma seria da seguinte maneira
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))

# posso enumerar as variaveis de acordo com a ordem que esta apresentada no format iniciando pelo zero
# fazendo com que consiga inverter as ordens
print('{0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))


