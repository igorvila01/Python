"""
Operadores aritmeticos
+  -  soma
-  -  subtracao
*  -  multiplicação
/  -  divisao
// -  Resultado da divisao fica inteiro, é arredondado
** -  Exponenciação (um numero elevado a outro)
%  -  Retorna o resto da divisão
() -  como na matematica, serve para alterar a ordem da operação
"""
print('Multiplicação * ', 10*10)

# Quando multiplicamos uma string, o operador se torna uma repetição
# No caso abaixo vai repetir o nome Igor 10 vezes
print('Multiplicação * ', 10 * 'Igor')
#---------------------------------------------------------------------

print('Adição + ', 10+10)
# Quando fazemos uma soma de string o operador vai concatenar as 2 strings
print('Concatenar ', 'Igor' + ' Vila')
# Caso queira concatenar um numero Inteiro, deve fazer a conversao para String
print('Igor Vila ' + 'tem ' + str(30) + ' anos')
# Esse tipo de concatenação é raramente utilizado em python
# ------------------------------------------------------------------------------

print('Subtração - ', 10-5)
print('Divisão / ', 10/2)
print('Divisão Inteiro', 11//6)  # Nesse caso vai truncar o valor para inteiro
print('Potencia', 10**2)
print('Resto da Divisao', 10%3)

# Como na matematica, vai fazer a multiplicação primeiro
print('Precedencia ', 5+2*10)  # resultado 25
# Caso queira mudar a precedencia do calculo, deve se utilizar parenteses, como na matematica
print('Precedencia ', (5+2)*10)  # Resultado 70