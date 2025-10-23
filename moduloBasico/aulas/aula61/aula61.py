"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

while True:
    cpf = input('Digite um CPF: ')
    numeros = cpf.replace('.','').replace('-','')
    nove = numeros[0:9]
    primeiro_digito = numeros[-2]

    if len(numeros) != 11:
        print('CPF nao possui 11 caracteres!')
        continue

    try:
        numeros = int(numeros)
        primeiro_digito = int(primeiro_digito)
    except ValueError:
        print('CPF digitado nao tem um formato valido!')
        continue     

    contador = 0
    mult = []
    for i in range(10,1,-1):        
        mult.append(i*int(nove[contador]))      
        contador += 1   

    soma = sum(mult)
    mult_10 = soma*10 
    resto_11 = mult_10 % 11

    if resto_11 > 9:
        resultado_d1 = 0
    else:
        resultado_d1 = resto_11
    
    if resultado_d1 == primeiro_digito:
        print(f'Primeiro digito: {primeiro_digito}\n'
              f'Digito verificado {resultado_d1} ')
        print('Primeiro digito é valido!')
    else:
        print(f'Primeiro digito: {primeiro_digito}\n'
              f'Digito verificado {resultado_d1} ')
        print('Primeiro digito invalido!')  

    break



    
    
   
    

