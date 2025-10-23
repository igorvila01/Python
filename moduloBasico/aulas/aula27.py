"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá Mundo!'

# começando de zero vou pegar a letra u da variavel 
print(variavel[5])

# pego o indice da direita para a esquerda com o sinal negativo
print(variavel[-4])

# Colocando a posição e ir até o final, é so colocar os 2 pontos, omitindo o final ele pega ate o final da string 
print(variavel[4:])

# quando queremos pegar apenas uma parte do texto, o numero apos os 2 pontos vai pegar o indice que voce digitou menos 1 caracter 
# Sempre pegar um a mais do que to pedindo para pegar o bloco desejado 
print(variavel[4:8])

# Omitindo o inicio, ele vai pegar sempre do começo 
print(variavel[:5])

# A função len é utilizada para a contagem de caracter, verificar o tamanho da string
# Pode ser utilizada com outros tipos tambem, mas vai ser feito nas proximas aulas 
print(len(variavel))

# O terceiro fatiamento é o passo serve para pular caracter em uma sequencia 
print(variavel[0:len(variavel):2])

# caso coloque o passo negativo, ele conta de traz pra frente 
print(variavel[::-1])





