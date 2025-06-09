'''
 Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso

 '''
from time import sleep

valor1 = int(input('Digie um numero: '))
valor2 = int(input('Digite outro valor: '))

somar = valor1 + valor2
multiplicar = valor1 * valor2

while True:
    sleep(1)
    print('[1] Somar' ,'\n[2] Multiplicar', '\n[3] Qual valor e maior', '\n[4] Novos números', '\n[5] Sair do programa')

    opcao = int(input('Digite a sua opção '))


    if opcao == 1:
        print(f'A soma do {valor1} com o {valor2} é {somar}')
        
    elif opcao == 2:
        print(f'A multiplicação do {valor1} com o {valor2} e {multiplicar}')

    if opcao == 3:
        if valor1 > valor2:
            print(f'O numero maior entre {valor1} e {valor2} é {valor1}')
        
        elif valor2 > valor1:
            print(f'O numero maior entre {valor1} e {valor2} é {valor2}')

        else:
            print(f'Os numeros {valor1} e {valor2} são iguais')

    elif opcao == 4:
        valor1 = int(input('Digite um novo valor: '))
        valor2 = int(input('Digite o segundo novo valor: '))

    elif opcao == 5:
        print('Você escolheu sair do jogo', '\n SAINDO...')
        sleep(4)
        print('FIM')
        break
    
    if opcao > 5 or opcao < 1:
        print('você não digitou uma opção valida')

