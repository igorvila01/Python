"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

a = 0
b = 1
contador = 20

while contador > 0:
    print(a)
    proximo = a + b
    a = b
    b = proximo
    contador -= 1