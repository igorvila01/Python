# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 1, 2, 3,3,3,1]
# s1 = set(l1)  
# l2 = list(s1)
# print(l2)

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Igor')
s1.add(1)
# update pode ser usado para mandar varios valores, cuidado com o iteravel que vai passar
# pois no caso de string ele separa letra por letra, por isso que no exemplo passei dentro
# de uma tupla 
s1.update(('Ola Mundo',1,2,3,4))
# para eliminar um item do set, como nao tem index, voce passa o valor que quer apagar
s1.discard('Ola Mundo')
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2

# mostrar somente o que esta presente nos 2 sets 
s3 = s1 & s2
# mostrar apenas os itens que estao no item da esquerda 
s3 = s1 - s2
# mostrar itens que estao presente em cada set 
s3 = s1 ^ s2
print(s3)