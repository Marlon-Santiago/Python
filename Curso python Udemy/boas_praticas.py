'''
CONSTANTES = Variaveis que não vao mudar e sempre colocalas em maiusculo
muitas consiçoes no mesmo if (RUIM)
    <--- Contagem de complexidade (RUiM)
'''

velocidade = int(input('Digite a sua velocidade: ')) # velocidade do carro e variavel não constante
local_carro = int(input('ESCOLHA O LOCAL DO CARRO ENTRE 99, 100 E 101')) # Local aonde o carro se encontra e variavel não constante

RADAR_1 = 60 # VELOCIDADE MAXIMA DO RADAR 1 E VARIAVEL CONSTANTE
LOCAL_1 = 100 # LOCAL AONDE O RADAR ESTAR E VARIAVEL CONSTANTE
RADAR_RANGE = 1 # A DISTANCIA QUE O RADAR PEGA E VARIAVEL CONSTANTE


if velocidade > RADAR_1 and local_carro >= LOCAL_1 + 1:
    print('Você passou pelo radar 1 acima da velocidade permitida')

elif velocidade <= RADAR_1 and local_carro >= LOCAL_1:
    print('Você passou na valecidade permitida pelo radar 1')

else:
    local_carro <= LOCAL_1
    print('Ainda não passou pelo radar 1')
