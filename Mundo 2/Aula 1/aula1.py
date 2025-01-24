valorc = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario do comprador: '))
ano = int(input('Digite em quantos anos ele quer pagar: '))

porcentagem = ((30 * salario) / 100)
prestaçao = valorc / (ano * 12)

if prestaçao <= porcentagem:
    print('Você pode fazer o emprestimo')

else:
    print('Você não pode pegar o emprestimo')