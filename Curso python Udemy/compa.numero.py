valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

if valor1 > valor2:
    print(f'O primeiro valor {valor1} e maior que o segundo valor {valor2}')

elif valor2 > valor1:
    print(f'O segundo valor {valor2} é maior que o primeiro valor {valor1}')

elif not valor1 and not valor2:
    print(f'Você não digitou nada preencha os campos corretamenta')

else:
    print(f'Os valores são iguais')



numero1 = input('Digite um número: ')
numero2 = input('Digite outro numero: ')

if numero1 > numero2 and numero1.isdigit() and numero2.isdigit():
    print(f'O numero {numero1} e maior que o número {numero2}')

elif numero2 > numero1 and numero2.isdigit() and numero1.isdigit():
    print(f'O número {numero2} é maior que o número {numero1}')

elif numero1 == numero2 and numero1.isdigit() and numero2.isdigit():
    print(f'Os números são iguais')

elif not numero1 and not numero2:
    print(f'Você não preencheu os campos com números')

else:
    print(f'por favor digite apenas números')

