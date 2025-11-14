def calcular_imc(peso, altura):
    peso = float(peso)
    altura = float(altura)
    imc = peso/(altura**2)
    return imc
    
def classificar_imc(imc):
    imc = float(imc)
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc >= 18.5 and imc <= 24.9:
        return 'Peso Normal'
    elif imc >= 25 and imc <= 29.9:
        return 'Sobrepeso'
    elif imc >= 30 and imc <= 34.9:
        return 'Obesidade Grau 1'
    elif imc >= 35 and imc <= 39.9:
        return 'Obesidade Grau 2'
    else:
        return 'Obesidade Grau 3'
    
while True:
    try:
        peso = float(input('Digite o seu peso: '))
        altura = float(input('Digite a sua altura: '))
    except ValueError:
        print('❌ Dados Invalidos! Digite novamente!')
        continue
    
    imc = calcular_imc(peso,altura)
    print(f'Seu imc é: {imc:.2f}')
    print(classificar_imc(imc))


    break
    
