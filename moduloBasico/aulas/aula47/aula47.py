
import os

def limpar_tela():
    os.system('cls')

palavra = 'perfume'.lower()
letras_digitadas = ''
acertos = ''
tentativas = 0

while True:
    
    # Mostrar letras digitadas e tentativas     
    print(f'Letras digitadas: {letras_digitadas}')
    print(f'Tentativas: {tentativas}')  

    palavra_oculta = ''
    #  Verificar a posição da letra
    for letra in palavra:        
        if letra in acertos:
            palavra_oculta += letra
        else:
            palavra_oculta += '_'
    print('')
    print(f'Palavra: {palavra_oculta}')
    print('')
    
    #  Verificar se a palavra terminou, caso nao tenha terminado, continua o laço 
    if '_' not in palavra_oculta:
        limpar_tela()
        print(f'PARABÉNS, VOCE GANHOU !!!! \nA palavra era: "{palavra_oculta}" e voce acertou em {tentativas} tentativas')
        break
    else:
        entrada = input('Digite uma letra: ').lower()
        print('')     

        #  Tratamento para letras digitadas em duplicidade, ou se digitar algum caracter que nao é letra 
        # Gravar as letras digitadas e quantidade de tentativas
        if entrada.isalpha() and len(entrada) == 1:
            if entrada in letras_digitadas:
                limpar_tela()
                print('Erro: Você já tentou essa letra. Tente outra!')
                continue
            else:
                if entrada in palavra:        
                    acertos += entrada
                    letras_digitadas += entrada
                    tentativas += 1 
                    limpar_tela()               
                    continue
                else:
                    letras_digitadas += entrada
                    tentativas += 1 
                    limpar_tela() 
                    continue
        else:
            limpar_tela()
            print('Erro: Entrada Invalida, por favor digite apenas uma letra!')
            continue


    