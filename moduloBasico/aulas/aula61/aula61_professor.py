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
import os
import re
import sys

def limpa_tela():
    os.system('cls')   

def finalizar():
    sys.exit() 

while True:
    
    cpf = input('Digite um CPF: ')
    # cpf_str = cpf.replace('.','').replace('-','').replace(' ','')
    cpf_str = re.sub(r'[^0-9]','',cpf)
    nove = cpf_str[0:9]
    dez = cpf_str[0:10]
    
    entrada_sequencial = cpf_str == cpf_str[0]*len(cpf_str)

    if entrada_sequencial == True:
        limpa_tela()
        print(f'O CPF {cpf_str} é Inválido!')
        finalizar()
    
    print(entrada_sequencial)

    if len(cpf_str) != 11:
        limpa_tela()
        print('CPF nao possui 11 caracteres!')
        continue

    try:
        cpf_str = int(cpf_str)
        # primeiro_digito = int(primeiro_digito)
        # segundo_digito = int(segundo_digito)
    except ValueError:
        limpa_tela()
        print('CPF digitado nao tem um formato valido!')
        continue     

# Primeiro digito ------------------------------------------------------
    cont_reg_d1 = 10
    soma_d1 = 0
    for d1 in nove: 
        soma_d1 += int(d1)*cont_reg_d1  
        cont_reg_d1 -= 1     
    resultado_d1 = (soma_d1*10) % 11

    resultado_d1 = resultado_d1 if resultado_d1 <= 9 else 0

# Segundo Digito-------------------------------------------------------
    cont_reg_d2 = 11
    soma_d2 = 0
    for d2 in dez:
        soma_d2 += int(d2)*cont_reg_d2
        cont_reg_d2 -= 1
    resultado_d2 = (soma_d2*10) % 11
    resultado_d2 = resultado_d2 if resultado_d2 <= 9 else 0

    cpf_verificado = nove+str(resultado_d1)+str(resultado_d2)
    if str(cpf_str) == cpf_verificado:
        print(f'O CPF {cpf_str} é válido!')
    else:
        print(f'O CPF {cpf_str} é inválido!')

    break



    
    
   
    

