"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABC'

print(f'{variavel}')

# preencher com zero a esquerda ou qualquer caracter que desejar o numero 10 significa a quantidade que vai ser completada como no exemplo ate chegar a 10 caracter
print(f'{variavel:0>10}')

# preencher com zero a direita ou qualquer caracter que desejar o numero 10 significa a quantidade que vai ser completada como no exemplo ate chegar a 10 caracter
print(f'{variavel:0<10}')

# deixar a variavel no meio e o restante preencher com zeros tanto na esquerda quanto direita 
print(f'{variavel:0^10}')

# Sinal de + na formatação do float serve para mostrar os sinais, caso coloque - ele só vai mostrar se o numero for negativo 
print(f'{-1000.6562632654962:+.1f}')

# O sinal de igual vai forção a formatação de sinal a aparecer antes dos zeros 
# mas tem outras formas mais faceis de deixar formatado 
print(f'{-1000.6562632654962:0=+10.1f}')

# o x maiusculo, mostra os hexadecimais maiusculos e o minusculo mostra minusculo 
print(f'O hexadecimal de 1500 é {1500:08X}')

# caso ver algum codigo na internet com essas flags !r, posso estar removendo que nao tem problema nenhum 
print(f'{variavel!r}')
