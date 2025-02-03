"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

nome = input('Digite o seu primeiro nome: ')

espaço = ' '

if len(nome) >= 1 and len(nome) <= 4:
    print(f'Seu nome {nome} é pequeno')

elif len(nome) >= 5 and len(nome) <= 6:
    print(f'Seu nome {nome} é normal')

elif len(nome) > 6:
    print(f'Seu nome {nome} é muito grande')

else: 
    not nome
    print('Você não digitou nada')
