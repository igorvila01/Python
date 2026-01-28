"""
- Mensagem inicial
Crie um decorador que imprime uma mensagem de "Iniciando execução..." antes de rodar qualquer função.
"""


# def cria_funcao(func):
#     def interna(*args, **kwargs):
#         print('Iniciando execução...')
#         result = func(*args, **kwargs)
#         return result
#     return interna

# @cria_funcao
# def saudacao():
#     print('Ola')

# @cria_funcao
# def soma(x,y):
#     print(x+y)
    
# saudacao()
# soma(1,2)


"""
- Tempo de execução
Crie um decorador que calcule e mostre quanto tempo uma função demora para rodar.

"""

# import time


# def tempo_execucao(func):
#     def interna(*args, **kwargs):
#         inicio = time.time()
#         result = func(*args, **kwargs)
#         fim = time.time()
#         print(f'Tempo de execução: {fim-inicio:.4f}')
#         return result
#     return interna

# @tempo_execucao
# def soma(x,y):
#     print(x+y)

# @tempo_execucao
# def inverter_string(texto):
#     print(texto[::-1])

# soma(999,9999)
# inverter_string('Igor')


"""
- Verificação de usuário
Crie um decorador que só permita executar a função se o usuário for "admin". Caso contrário, deve mostrar "Acesso negado".
"""

def verifica_usuario(func):
    ...

"""
- Repetição de execução
Crie um decorador que receba um parâmetro n e faça a função ser executada n vezes.

"""

"""
- Logger de argumentos
Crie um decorador que mostre os argumentos recebidos pela função antes de executá-la.

"""


"""
- Cache simples
Crie um decorador que armazene os resultados de uma função para evitar cálculos repetidos (exemplo: função que calcula fatorial).

"""


"""
- Composição de decoradores
Use dois decoradores diferentes em uma mesma função e observe a ordem de execução.

"""