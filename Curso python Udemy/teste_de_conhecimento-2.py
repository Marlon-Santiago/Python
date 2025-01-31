'''
Faça um progama que peça ao usuarioa para digitar um número inteiro,
Informe se ele e par ou impar e se o usario nao digitou nada ou um numero não inteiro

'''


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


# Correção do exaercicio feita pelo professor

#entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}')

# else:
#     print('Você não digitou um número inteiro')


#try:
#    entrada_int = float(entrada)
#    par_impar = entrada_int % 2 == 0
#    par_impar_texto = 'ímpar'

#    if par_impar:
#        par_impar_texto = 'par'
#    print(f'O número {entrada_int} é {par_impar_texto}')

#except:
#    print('Você não digitou um número inteiro')