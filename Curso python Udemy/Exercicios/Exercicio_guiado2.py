while True:

    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Escolha um desses operadorres [+-/*]: ')

    numero_valido = None

    try:
        numero_1 = float(numero1)
        numero_2 = float(numero2)
        numero_valido = True

    except:
        numero_valido = None

    if numero_valido is None:
        print('Um ou ambos números digitados e/ou são invalido')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Digite um operador valido')

    if len(operador) > 1:
        print('Digite apenas um operador por calculo')


    sair = input('Quer sair ? Digite sim: ').lower().startswith('s')

    if sair is True:
        break
print('Você saiu')