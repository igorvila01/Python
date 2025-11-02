"""
Exercicio com funçoes 

Crie uma função que mutiplica todos os argumentos 
não nomeados recebidos
Retorne o total para uma variavel e mostre o valor da variavel
"""
print(5*6*7*8*9*10)

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
        resultado = "Numero Par"
        return resultado
    else:
        resultado = 'Numero Impar'
        return resultado


print(par_impar(1))


