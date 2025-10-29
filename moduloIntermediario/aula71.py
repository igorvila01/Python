"""
args - Argumentos nao nomeados 
* - *args (empacotamento e desempacotamento)
"""

# lembre-te de desempacotamento 
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

# print(1, 2, 3, 4, 5)
# Args é utilizado para declarar uma quantidade de parametros ilimitados, lembrando que sera empacotado e 
# transformado em uma tupla 
def soma(*args):
    total = 0
    for numero in args:
        total += numero
        # print(numero, total)
    return total
    
numeros = 1, 2, 3
soma123 = soma(*numeros)
print(soma123)

soma456 = soma(4, 5, 6)
print(soma456)