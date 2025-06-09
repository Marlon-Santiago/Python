'''
n = 1
r = 1

while n != 0:
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()

    print('Fim do programa') 

'''
'''
n = 1
pa = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))

    if n != 0:

        if n % 2 == 0:
            pa += 1

        else:
            impar += 1

print(f'Você digitou {pa} números pares e {impar} números ímpares.')
# Fim do programa
print('Fim do programa')

'''

while True:
    nome = input('digite o nome de quem criou esse programa: ').capitalize()

    if nome != 'Marlon':
        print('Você errou')

    else:
        print('parabens')
        break

