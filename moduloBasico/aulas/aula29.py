"""
Introdução ao Try/Except

try -> Tentar executar o codigo 
except -> Ocorreu algum erro ao tentar executar 

Aula somente o basico
"""
numero_str = input('Vou dobrar o numero que voce digitar: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro de {numero_str} é {numero_float*2:.2f}')
except:
    print('Isso nao é um numero!')

# isdigit, verifica se o usuario digitou apenas numeros 
# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float*2:.2f}')
# else:
#     print('Isso nao é um numero!')
