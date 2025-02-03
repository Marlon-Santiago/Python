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
    
    if hora <= 11:
        print(f'Bom Dia !!!!!, São {hora}:{minutos}:{segundos}')

    elif hora > 11 and hora <= 17:
        print(f'Boa Tarde !!!!!, São {hora}:{minutos}:{segundos}')
    
    elif hora > 17 and hora <= 23:
        print(f'Bom Noite !!!!!, São {hora}:{minutos}:{segundos}')

else:
    print('Você não digitou um número válido')


