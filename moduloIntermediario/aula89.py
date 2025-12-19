# di, hasattr e getattr em python
string = 'Igor'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Nao Existe upper')
