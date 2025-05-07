
soma = 0
cont = 0

for c in range(1, 7):
    numero = int(input('Digite um numero inteiro:'))

    if numero % 2 == 0:
        soma += numero
        cont += 1

print(f'A Soma dos numeros pares digitados é {soma} e a quantidade é {cont}')
        

