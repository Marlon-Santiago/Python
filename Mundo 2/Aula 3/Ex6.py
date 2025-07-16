'''
Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

termo = int(input('Digite o preimeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 1
mais = 10
total = 0
while mais != 0:
    total += mais

    while contador <= total :
        print(termo, end = ' --> ', )
        termo += razao
        contador += 1
    print('Pausa')

    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados.')