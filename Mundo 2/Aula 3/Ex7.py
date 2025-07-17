'''
Exercício Python 063: Escreva um programa que leia um número N inteiro 
qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
'''

termos = int(input('Quantos termos você quer mostrar? '))

fibonacci = [0, 1]  # Iniciando a lista com os dois primeiros termos da sequência de Fibonacci

while len(fibonacci) < termos:
    proximo_termo = fibonacci[-1] + fibonacci[-2] # Calcula o próximo termo somando os dois últimos termos
    fibonacci.append(proximo_termo)

print('Sequencia de Fibonacci: ')
print(fibonacci) # Exibe a sequência de Fibonacci até o número de termos solicitado