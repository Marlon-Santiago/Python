'''
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador 
vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.

'''

import random

numero_aleatorio = random.randint(1, 10)
tentativa = 0
numero = int(input('Digite um numero de 1 a 10: '))

while numero != numero_aleatorio:
    numero = int(input('Você errou digite novamente um numero de 1 a 10: '))
    tentativa += 1

    if numero == numero_aleatorio:
        print(f'Você acertou depois de {tentativa} tentativas')
        break