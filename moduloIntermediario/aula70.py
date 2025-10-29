"""
Retorno de valores das funçoes (return)
"""

# Por padrao as fnçoes do python retornam none, caso queira que retorne algum valor devo usar o return 
# Apos retornar um valor, nao posso declarar mais nada na função, porque é como se definisse o final da função
def soma(x,y):
    if x > 10:
        return [10, 20]
    return x + y
    

soma1 = soma(1, 2)
soma2 = soma(3, 5)
print(soma1)
print(soma2)
print(soma(11, 55))
