# Try, except, else e finally


try:
    a= 18
    b = 0
    print(b[0])
    print('linha 1')
    c= a/b
except ZeroDivisionError:
    print('Voce tentou dividir por zero ')

except NameError:
    print('Nome b nao esta definido')

# Posso adicionar duas exceçoes em um mesmo except, colocando-os em uma tupla 
# as vai criar um alias para a exceção, para ser mostrado posteriormente o erro que ocorreu 
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG: ', error)
    print('Nome: ',error.__class__.__name__)

# Exception vai tratar qualquer erro que der na execução do try 
except Exception:
    print('Erro desconhecido')


    