"""
Exercicio com funçoes 

Crie uma função que mutiplica todos os argumentos 
não nomeados recebidos
Retorne o total para uma variavel e mostre o valor da variavel
"""


def multiplica(*args):
    total = 1   
    for numero in args:               
        total *= numero
    return total

numeros = 5, 6, 7, 8, 9, 10
resultado = multiplica(*numeros)
print(resultado)


"""
Crie uma função fala se um numero é par ou impar.
Retorne se um numero é par ou impar.
"""


def par_impar(x):
    if x % 2 == 0:        
        return f'{x} é Par'
    
    return f'{x} é Impar'


print(par_impar(2))


