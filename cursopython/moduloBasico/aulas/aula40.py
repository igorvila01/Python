"""
Calculadora com while
"""

while True:     
    num1 = input('Digite o primeiro numero: ') 
    num2 = input('Digite o Segundo numero: ')
    operador = input('Digite o Operador (+-/*): ')  

    valida_numeros = None     

    try:
        num1 = float(num1)
        num2 = float(num2)
        valida_numeros = True        
    except:
        valida_numeros = None

    if valida_numeros is None:
        print('Um ou ambos numeros sao Invalidos!')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos and len(operador) > 1:
        print('Operador invalido!')
        continue
    else:
        soma = num1+num2
        subtracao = num1-num2
        multiplicacao = num1*num2
        divisao = num1/num2

        if operador == '+':
            print(f'A soma dos numeros é: {soma}')
        elif operador == '-':
            print(f'A subtração dos numeros é: {subtracao}')
        elif operador == '*':
            print(f'A multiplicação dos numeros é: {multiplicacao}')
        elif operador == '/':
            print(f'A Divisao dos numeros é: {multiplicacao}')
        else:
            print('Operador Invalido!')   
    # lower somente letra minuscula e startswith é como se fosse um if para primeira letra 
    sair = input('Quer sair? [s]sim: ').lower().startswith('s')  

    if sair is True:
        print('Voce saiu da calculadora !')
        break

