import copy
import os
# copy, sorted, produtos.sort
# Exercícios

def limpa_tela():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Linux / Mac
    else:
        os.system('clear')

from dados_aula_100 import produtos
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)


limpa_tela()

print('Produtos Originais:')
print(*produtos, sep='\n')

novos_produtos = copy.deepcopy(produtos)
print('\nNovos Produtos: ')
for x in novos_produtos:
    x['preco'] = round(x['preco'] * 1.1,2)
    print(x)



# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
produtos_ordenados_por_nome.sort(key=lambda produtos: produtos['nome'], reverse=True)
print('\nProdutos ordernados por nome decrescente: ')
print(*produtos_ordenados_por_nome, sep='\n')
# for i in produtos_ordenados_por_nome:
#     print(i)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preco.sort(key=lambda produtos: produtos['preco'])
print('\nProdutos ordernados por preco crescente: ')
print(*produtos_ordenados_por_preco, sep='\n')