"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""

hora = input('Digite que horas: ')
minutos = input('Digite os minutos: ')
segundos = input('Digie os segundos: ')



if hora.isdigit() and minutos.isdigit() and minutos.isdigit():
    hora = int(hora)
    
    if hora >= 0 and hora <= 11:
        print(f'Bom Dia !!!!!, São {hora}:{minutos}:{segundos}')

    elif hora > 11 and hora <= 17:
        print(f'Boa Tarde !!!!!, São {hora}:{minutos}:{segundos}')
    
    elif hora > 17 and hora <= 23:
        print(f'Bom Noite !!!!!, São {hora}:{minutos}:{segundos}')

    elif hora > 23 or minutos > 59 or segundos > 59:
        print('O dia tem 24 horas os minutos vão ate 59 assim como os segundos digite os numeros dentro desses valores')

else:
    print('Você não digitou uma hora válida')

'''
CORREÇÃO DO PROFESOR

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
'''


