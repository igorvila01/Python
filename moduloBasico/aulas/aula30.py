"""
CONSTANTE = "Variaveis" que nao vao mudar 
Muitas condiçoes no mesmo if (ruim)
....<- Contagem de complexidade (ruim)

"""

velocidade = 60  # Velocidade atual do carro 
local_carro = 99  # local em que o carro esta na estrada 

# Variaveis constantes, nunca vai mudar os valores 
RADAR_1 = 60  # Velocidade do radar 1
LOCAL_1 = 100  # local onde o radar 1 esta 
RADAR_RANGE = 1  # A distancia onde o radar pega 

velocidade_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1-RADAR_RANGE) and \
                        local_carro <= (LOCAL_1+RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_pass_radar_1

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if carro_multado_radar_1:
    print(f'O carro foi multado em radar 1!')
else:
    print(f'Veiculo nao foi multado!')
