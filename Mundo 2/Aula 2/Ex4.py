numero = int(input('digite um numero eu mostrarei a tabuada de 1 a 10: '))

contado  = 0

for i in range(0, 11):
    resultado = numero * contado
    print(f'o resultado de {numero} x {contado} é {resultado}')
    contado = contado + 1