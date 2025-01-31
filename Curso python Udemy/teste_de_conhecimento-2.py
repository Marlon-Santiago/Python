# Faça um progama que peça ao usuarioa para digitar um número inteiro

numero = input('Digite um numero inteiro irei te dizer se ele é par ou impar: ')

nao_digitou_um_numero = numero.isdigit()
#numero_par = numero % 2 == 0

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'Esse número é par')
 
    elif int(numero) % 2 == 1:
        print('Esse numero é impar')

else:
    nao_digitou_um_numero == False
    print('Você não digitou nada ou não digitou um número inteiro')

print(nao_digitou_um_numero)