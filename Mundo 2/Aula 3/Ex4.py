# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

# import math

numero = int(input('Digite um numero: '))
cont = 1
res = 1

while cont <= numero:
    res *= cont
    print(f'{cont}! = {res}')
    cont += 1


    