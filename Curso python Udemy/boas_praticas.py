'''
CONSTANTES = Variaveis que não vao mudar e sempre colocalas em maiusculo
muitas consiçoes no mesmo if (RUIM)
    <--- Contagem de complexidade (RUiM)

Foi feito um codigo para saber a velocidade em que o carro passa no radar e se ele vai ser multado ou não
'''

velocidade = int(input('Digite a sua velocidade: ')) # velocidade do carro e variavel não constante
local_carro = int(input('ESCOLHA O LOCAL DO CARRO ENTRE 99 e 101: ')) # Local aonde o carro se encontra e variavel não constante

RADAR_1 = 60 # VELOCIDADE MAXIMA DO RADAR 1 E VARIAVEL CONSTANTE
LOCAL_1 = 100 # LOCAL AONDE O RADAR ESTAR E VARIAVEL CONSTANTE
RADAR_RANGE = 1 # A DISTANCIA QUE O RADAR PEGA E VARIAVEL CONSTANTE
FORA_DO_RADAR = 2

passou_acima_da_velocidade_no_radar1 = velocidade > RADAR_1
passou_na_velocidade_permitida_no_radar1 = velocidade <= RADAR_1
carro_passou_na_area_do_radar = local_carro >= LOCAL_1 - RADAR_RANGE or local_carro <= LOCAL_1 + RADAR_RANGE


if passou_acima_da_velocidade_no_radar1 and carro_passou_na_area_do_radar:
    print('O carro passou acima da velocidade permitida no radar 1 e foi multado')

elif passou_na_velocidade_permitida_no_radar1 and carro_passou_na_area_do_radar:
    print('O carro passou a 60 km/h ou abaixo velocidade permitida')
