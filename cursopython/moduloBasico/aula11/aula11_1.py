"""
Metodo len só funciona com strings e float
"""

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi {len(string1)+len(string2)}')

# duas maneiras de chamar o metodo len
print(len(string2))
print(string2.__len__())
