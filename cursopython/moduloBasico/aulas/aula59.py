# Desempacotamento em chamadas 
# de metodos e funçoes 

string = 'ABCD'
lista = ['Maria', 'Helena',1,2,3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# a,b,*_,ap, u = lista
# print(a,u,ap)

# for nome in lista:
#     print(nome, end=' ')

print(*lista)
print(*string)
print(*tupla)
