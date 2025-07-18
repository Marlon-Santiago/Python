'''
Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

media = 0
contador = 0
soma = 0
maior = 0
menor = 0

while True:
    numero = int(input('Digite um número: '))

    if contador == 0:
        maior = numero
    
    if numero > maior:
        maior  = numero

    if contador == 0:
        menor = numero

    if numero < menor:
        menor = numero

    continuar = input('Deseja continuar ? [S/N]').upper()
    contador += 1
    soma += numero


    if continuar == 'N':
        break

print(f'Você digitou {contador} e a média foi {soma / contador}' )
print(f'O maior numero digitado foi {maior} e o menor digitado foi {menor}')

    

