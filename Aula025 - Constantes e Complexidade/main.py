"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = input('Velocidade do carro:') # velocidade atual do carro

local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_carro_radar = velocidade > RADAR_1
carro_passou_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar = carro_passou_radar and velocidade_carro_radar

if velocidade_carro_radar:
    print('Carro ultrapassou a velocidade máxima.')

if carro_passou_radar:
    print('Carro passou no radar 1')

if carro_multado_radar and velocidade_carro_radar:
    print('Carro foi multado no radar 1')