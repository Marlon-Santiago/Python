nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f'\033[7;31;40m{nome} está magro procura ajuda médica \033[m')

elif imc <= 24.9:
    print(f'\033[7;32;40m{nome} está no peso normal \033[m')

elif imc <= 29.9:
    print(f'\033[7;36;47m{nome} está com sobrepeso \033[m')

elif imc <= 39.9:
    print(f'\033[7;34;47m{nome} está com obesidade grau 2 \033[m')

else:
    print(f'\033[7;35;40m{nome} esta com obesidade grau 3 procure um medico \033[m')
