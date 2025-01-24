numero = int(input('Digite um numero: '))

print('Digite 1 para converter para binario')
print('digite 2 para comverta para octal')
print('Digite 3 para converter para hexadecimal')

conversao = int(input('Escolha um numero para fazer a conversão'))

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if conversao == 1:
    print(f'O numero digitado foi {numero} e ele convertido é {binario[2:]}')

elif conversao == 2:
    print(f'O numero digitado foi {numero} e sua conversão para octal é {octal[2:]}')

else:
    conversao == 3
    print(f'O numero digitado foi {numero} e sua conversão para hedecimel é {hexadecimal[2:]}')
