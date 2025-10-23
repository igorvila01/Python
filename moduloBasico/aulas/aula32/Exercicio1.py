"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario não digita um numero inteiro, 
informe que nao é um numero inteiro.
"""

# ------------Uma forma de ser feito  mais robusto do que o segundo -------------------------------
try:
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        print(f'O numero informado {numero} é par!')
    else:
        print(f'O numero informado {numero} é impar!')
except:
    print('Numero informado nao é inteiro!')


# --------- Segunda Forma de ser feito Simples, pois o is digit nao aceita numero negativos-------------------------
# numero = input('Digite um numero: ')

# if numero.isdigit():
#     numero_convert = int(numero)
#     if numero_convert % 2 == 0:
#         print(f'O numero informado {numero_convert} é par!')
#     else:
#         print(f'O numero informado {numero_convert} é impar!')      
# else:
#     print('Numero digitado nao é inteiro! ')


