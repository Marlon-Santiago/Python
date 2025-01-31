nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = int(input('Digite seu peso: '))

imc = peso / (altura * altura)

print(f'{nome} tem {altura} de altura e pesa {peso} e seu IMC é de {imc}')