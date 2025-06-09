''' 
Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores 'M' ou 'F'. Caso esteja errado, 
peça a digitação novamente até ter um valor correto.

'''

while True:
    sexo = input('Digite seu sexo [F/M]: ').upper().strip()[0]

    if sexo == 'F' or sexo == 'M':
        print(f'Sexo {sexo} registrado com sucesso')
        break

    else:
        print('sexo invldio. Digite seu sexo novamente')

