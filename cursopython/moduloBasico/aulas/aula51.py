"""
Introdução ao desempacotamento 
"""
# caso fosse 2 variaveis e 3 dados, ia dar erro que nao tem dados suficientes para preencher as variaveis 
# Mesma coisa se tiver dados a mais que variaveis 
# nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
# print(nome2)

# Sempre que for pegar um valor , sempre informar o que vai fazer com o restante da lista 
# Geralmente essa variavel voce nao vai usar ela, entao sempre que tiver uma variavel assim, declare ela como underline
# nome1, *_ = ['Maria', 'Helena', 'Luiz']
# print(nome1)

# Se quiser pegar algo do meio, usar underline antes 
_,nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2)