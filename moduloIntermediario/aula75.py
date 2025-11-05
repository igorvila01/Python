"""
Exercicios 
Crie funçoes que duplicam, triplicam e quadruplicam 
o numero recebido como parametro 
"""
# Minha operacao
# def operacao(num):
#     print(num)
#     for numero in range(2,5):
#         print(f'{num} x {numero} = {num*numero}')

# operacao(2)

# operacao do professor
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))