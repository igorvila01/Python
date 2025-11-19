"""
🧩 Desafio: Cadastro de Produtos e Estoque
Objetivo
Criar um programa que:
- Solicite ao usuário quantos produtos serão cadastrados.
- Para cada produto, peça nome, preço e quantidade em estoque.
- Use funções para:
- cadastrar_produto → retorna um dicionário com os dados do produto.
- calcular_valor_total → calcula o valor total em estoque (preço × quantidade).
- exibir_relatorio → mostra todos os produtos cadastrados com seus valores.
"""
def cadastrar_produto(nome, preco, estoque, total):
    nome = str(nome)
    preco = float(preco)
    estoque = float(estoque)
    total = float(total)
    produto = {
                'nome' : nome,
                'preco_unitario' : round(preco, 2),
                'qtd_estoque' : round(estoque,3),
                'valor_total' : round(total, 2)
            }

def calcular_valor_total(preco, quantidade):
    preco = float(preco)
    quantidade = float(quantidade)
    total = preco*quantidade
    return total

produtos = []
while True:
    try:
        qtd_itens = int(input('Qual a quantidade de produtos que será cadastrado?\n'))  
        break
    except ValueError:
        print('❌ Entrada invalida! Digite um numero inteiro!')
        continue

for i in range(qtd_itens):
    while True:
        try: 
            nome = str(input(f'Digite o produto {i+1}:\n'))
            preco_unitario = float(input(f'Digite o preço unitario do produto {i+1}:\n'))
            qtd_estoque = float(input(f'Quantidade estoque produto {i+1}:\n'))

            valor_total = calcular_valor_total(preco_unitario, qtd_estoque)
            produto = cadastrar_produto(nome, preco_unitario, qtd_estoque, valor_total)

            produtos.append(produto)
            break
        except ValueError:
            print('❌Entrada Invalida! Digite novamente!')
            continue

print(produtos)