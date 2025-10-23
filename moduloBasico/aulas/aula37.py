"""
Repetiçoes 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira 
"""

contador = 0

while contador <= 100:    
    contador += 1  # Sempre lembrar de colocar o contador para nao ter loop infinito 
    

    if contador == 6:
        print('Nao vou mostrar o 6')
        continue   # Continue Serve pra pular alguma sequencia dentro do while

    if contador >= 10 and contador <= 30:
        print('Nao vou mostrar o ',contador)
        continue

    print(contador) 

    if contador == 40:         
        break  # Serve para parar o while 
    
print('Acabou!')




