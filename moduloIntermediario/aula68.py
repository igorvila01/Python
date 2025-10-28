"""
Escopo de funçoes em python 
Escopo significa o local onde aquele codigo pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o codigo é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local 
podem ser alcançados.
"""

x = 1

def escopo():
    # Se eu defino uma variavel x dentro da função e fora tambem tem uma variavel x, essa que esta dentro 
    # da função nao tem nada a ver com a de fora 
    # Se definir x como global, posso altera-lo de fora da função 
    global x
    x = 10
    def outra_funcao():
        # Y só pode ser acessado dentro dessa outra função 
        global x
        y = 2
        x = 11
        print(x,y)
    # outra_funcao só pode ser chamada dentro da função escopo 
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)