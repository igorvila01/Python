"""
Exercicios 
Crie funçoes que duplicam, triplicam e quadruplicam 
o numero recebido como parametro 
"""
def operacao(num):
    print(num)
    for numero in range(2,5):
        print(f'{num} x {numero} = {num*numero}')

operacao(2)
