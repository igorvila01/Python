"""
Valores padrao para parametros 
Ao definir uma função, os parametros podem 
ter valores padrao. Caso o calor nao seja 
enviado para o parametro, o valor padrão sera 
usado 
Refatorar: editar o seu codigo.
"""
# zero é considerado valor false, nesse caso usamos none com um if verificando se nao é none
# todo parametro que vem depois de um valor padrao, vou precisar informar um valor padrao 
def soma(x, y, z=None):
    if z is not None:       
        print(f'{x=} {y=} {z=}',x + y + z)
    else:
        print(f'{x=} {y=} ',x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(100, 200, 0)
soma(x= 100, z= 200, y= 7)