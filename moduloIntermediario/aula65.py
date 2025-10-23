"""
introdução as funçoes (def) em python 
Funçoes sao trechos de codigo usado para 
replicar determinada ação ao longo do seu codigo 
Elas podem receber valores para parametros (argumentos)
e retornam um valor especifico .
por padrao, funçoes python retornam none(nada)
"""
# def Mostrar():
#     print('varias')

# Mostrar()


# Padrao para funçoes no python sempre começar com letra minuscula 
# Parametros são o que fica entre parenteses de uma funçao 
# def imprimir(a,b,c):
#     print(a,b,c)

# # Cada chamada de função posso mudar os parametros 
# imprimir(1,2,3)
# imprimir(4,5,6)

# Definindo um valor defaulta para o parametro nome, ao chamar a função e nao informar o parametro, 
# o sistema entende que deve chamar o valor padrao
def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')

saudacao('Igor')
saudacao()
