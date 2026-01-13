
import aula98_m



# quando importamos um modulo, e queremos fazer um laço de repetição de um dado
# devemos utilizar outro tipo de importacao para ser recarregado, pois caso contrario 
# vai mostrar apenas uma vez, e para isso utilizamos importlib juntamente com a funcao
# reload
import importlib


print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)

print('fim')