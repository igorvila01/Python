"""
Tipos de Dados
str - String - Texto 'Assim' "Assim"
int - Inteiro - 123456
float - real /Ponto flutuante - 10.50 1.5 -10.10
bool - Booleano/ logico - True/False 10 == 10   Obs: Sempre com inicial maiusculo
"""

print('Igor', type('Igor'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))
print('L' == 'L', type('L' == 'L'))
print(bool([]))

#--------------------------------------------------
print('Igor', type('Igor'), bool('Igor'))
print('10', type('10'), type(int('10')))

print('-------------------Cadastro---------------------------')
print('')
# Nome - str - type vai mostrar o tipo que foi digitado, nesse caso seria uma string
print('Igor Vila', type('Igor Vila'))
#Idade - int - type vai mostrar o tipo que foi digitado, no caso seria um numero inteiro
print(30, type(30))
#Altura - float - nesse caso o type vai mostrar que o tipo é inteiro
print(1.87, type(1.87))

#É maior de idade > 18 - Nesse caso o type vai mostrar um tipo boolean, comparando se a idade de 30 anos é maior que 18
print(30 > 18, type(30>18))

