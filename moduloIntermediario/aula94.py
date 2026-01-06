# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
# Try nao pode ficar sozinho 
try:
    print('Abrir arquivo')
    8/0

# Posso ter quantos excepts quiser 
except ZeroDivisionError as e:
    print(e.__class__.__name__)  #Capturar o nome do erro 
    print(e)  # Captura a mensagem do erro 
    print('Dividiu Zero')
# finally sempre sera executado, mesmo que ocorra um erro 
else:
    print('Nao deu erro')
finally:
    print('Fechar arquivo')