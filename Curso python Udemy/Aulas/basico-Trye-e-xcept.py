'''
try --> tenta executar o código
except --> ocorreu alfum erro ao tentar executar
'''


numero_str = input('Vou dobra o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')

except:
    print('Isso não e um número')
