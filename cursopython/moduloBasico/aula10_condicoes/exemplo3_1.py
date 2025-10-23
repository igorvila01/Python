"""
Operadores logicos
and    - e
or     - ou
not    - nao         = usado para inverter expressao e quando quer que preencha algum valor que esta zerado 
in     - em
not in - não contem
"""



a = 2
b = 3
c = 0

if not c:
    print('Por favor preencha o valor de C')
else:
    print('A é maior que B')


variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)