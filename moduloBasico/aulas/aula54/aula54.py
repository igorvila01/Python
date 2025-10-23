"""
Faça uma lista de compras com listas 
O usuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista 
Nao permita que o programa quebre com 
erros de indices inexistentes na lista 
"""
import os

def limpar_tela():
    os.system('cls')

lista = []

while True:    
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()   
    
    if opcao not in 'ails' and opcao.isalpha() == False:
        print('Voce nao digitou uma opção valida!')
        continue

    if opcao[0].lower() == 'i':
        limpar_tela()
        valor = input('Valor: ')
        lista.append(valor)
        limpar_tela()
        continue

    elif opcao[0].lower() == 'l':
        limpar_tela()
        if len(lista) == 0:
            print('Nenhum item para listar')
            continue
        else:
            print('Sua lista de compras abaixo:')
            print('----------------------------')
            for indice, suprimento in enumerate(lista):
                print(indice, suprimento)
                continue
    
    elif opcao[0].lower() == 's':
        limpar_tela()
        if len(lista) == 0:
            print('Voce encerrou sua lista sem inserir nenhum item! ')
            break
        else:
            print('Sua lista de compras pronta abaixo:')
            print('-----------------------------------')
            for indice, suprimento in enumerate(lista):
                print(indice, suprimento)
            print('-----------------------------------')
            break

    elif opcao[0].lower() == 'a':
        limpar_tela()
        for indice, suprimento in enumerate(lista):
            print(indice, suprimento)        
        try:
            apaga = int(input('Escolha o indice para apagar: '))            
            lista.pop(apaga)
            limpar_tela()
            continue
        except ValueError:
            print('Por Favor digite um numero inteiro!')
        except IndexError:
            print('Indice nao existe!')
        except Exception:
            print('Erro Desconhecido!')

        
