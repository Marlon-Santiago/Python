'''
Exercício Python 067: Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo. 
'''
contador = fator = 0

while True:
    numero = int(input('Digite um número para ver sua tabuada: '))
    contador = fator = 0
       
    if numero < 0:
        break
    
    while contador < 11:
        resultado = numero * contador
        print(f'{numero} x {fator} = {resultado}')
        contador += 1
        fator += 1
   

'''
while True:
    n = int(input('Digite um número para ver sua tabuada: '))

    if n < 0:
        break

    for c in range(0, 11):
        print(f'{n} x {c} = {n*c}')
'''