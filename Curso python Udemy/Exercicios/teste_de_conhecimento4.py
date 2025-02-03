"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

nome = input('Digite o seu primeiro nome: ')

if len(nome) <= 2:
    print('Digite mais de 2 letras')

    if len(nome) >= 3 and len(nome) <= 4:
        print(f'Seu nome {nome} é pequeno')

    elif len(nome) >= 5 and len(nome) <= 6:
        print(f'Seu nome {nome} é normal')

    elif len(nome) > 6:
        print(f'Seu nome {nome} é muito grande')

else: 
    not nome
    print('Você não digitou nada')



'''

CORREÇÃO O PROFESSOR

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')

        else:
    print('Digite mais de uma letra.')

'''