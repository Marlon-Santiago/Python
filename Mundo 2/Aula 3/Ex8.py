'''
Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

flag = 0
total = 0
contador = 0

while flag != 999:
    total = total + flag
    contador += 1
    flag = int(input('Digite um número (999 para parar): '))

print(f'Foram digitados {contador - 1} e a soma é {total}')

'''
while True:
    flag = int(input('Digite um número (999 para parar): '))
    if flag == 999:
        break  
    total += flag
    contador += 1

print(f'A soma dos {contador} números digitados é {total}')

'''