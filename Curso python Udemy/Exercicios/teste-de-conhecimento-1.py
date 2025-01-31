nome = input('Digite seu nome: ')

idade = input('Digite sua idade: ')

if nome and idade :
    print(f'O seu nome é {nome} e sua idade é {idade}')
    print(f'Esse é o seu nome invertido {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome tem espaços')

    else:
        print('Seu nome não tem espaços')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    not nome or not idade
    print('Desculpe você deixou um dos campos vazios')

