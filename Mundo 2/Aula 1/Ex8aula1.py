preço = float(input('Digite o valor da sua compra: '))

print('FORMAS DA PAGAMENTO')
print('Digite 1 para Pagamentro a vista ')
print('Digite 2 para pagamento a vista no cartão')
print('Digite 3 para pagamento parcelado em 2x no cartão')
print('Digite 4 para pagamento parcelado em 3x ou mais no cartão ')

pagamento = float(input('escolha uma forma de pagamento '))

dinheiro = (10 / 100) * preço
cartao = (5 / 100) * preço
cartão2 = (20 / 100) * preço

if pagamento == 1:
    print(f'pagando no dineiro você tem direito a 10% de desconto com isso de R$ {preço} você ira paga R$ {preço -  dinheiro}')

elif pagamento == 2:
    print(f'pagando no cartão avista você tem 5 % de desconto de R$ {preço} ira pagar {preço - cartao}')

elif pagamento == 3:
    print(f'pagando parcelado no cartão não temos desconto com isso você ira pagar R$ {preço} e cada parcela sera de R$ {preço / 2}')

elif pagamento == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    print(f'pagando no cartão em 3 x ou mais terar juros com isso você pagara R$ {preço + cartão2} e cada parcela sera de R$ {(preço + cartão2) / parcelas}') 




