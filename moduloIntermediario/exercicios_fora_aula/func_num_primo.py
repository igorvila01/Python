"""
Criar uma função que verifica se um numero é primo 

Utilize dessa função para mostrar os numeros primos de um determinado periodo de numeros 
"""

def verifica_primo(num):
    if num < 2:
        return False
    
    if num == 2:
        return True
    else:          
        for numero in range(2,num):
            if num % numero == 0:
                return False
        return True 

            
       
def periodo_primo(inicio, fim):
    primos = []
    for i in range(inicio,fim+1):
        if verifica_primo(i) == True:
            primos.append(i)
    return primos

print(periodo_primo(1,100))    

