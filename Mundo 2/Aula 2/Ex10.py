# Exercicio 10 - Faça um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# O nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

# Inicializa as variáveis
contidade = 0
maioridade = 0
homemmaisvelho = ''
mediaidade = 0

# Solicita os dados da pessoa
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    pessoa = input('Digite o nome da pessoa: ')
    idade = input('Digite a idade da pessoa: ')
    sexo = input('Digite o sexo da pessoa (M/F): ').upper()
    

# Verifica se a pessoa é do sexo feminino e tem menos de 20 anos
    if sexo == 'F':
        idade = int(idade)
        if idade < 20:
            contidade += 1

# Verifica se a pessoa é do sexo masculino e se é o homem mais velho    
    if sexo == 'M':
        idade = int(idade)
        if idade > maioridade:
            maioridade = idade
            homemmaisvelho = pessoa
    if not  (sexo, 'M', 'F'):
        print('Sexo inválido! Digite M ou F.')
    
    # Soma a idade para calcular a média
    mediaidade += int(idade)
        
        
print('----- RESULTADOS -----')
print(f'a media de idade é {mediaidade / 4} anos')    
print(f'O homem mais velho é {homemmaisvelho} com {maioridade} anos')
print(f'Ao todo, temos {contidade} mulheres com menos de 20 anos')
            

