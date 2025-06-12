frase = input('Digite uma frase: ')

indice = 0
nova_frase = ''

for c in frase:
    c = frase[indice]
    nova_frase += c
    indice+=1

nova_frase = nova_frase[::-1].replace(' ', '')
frase = frase.replace(' ', '')


if frase == nova_frase:
    print(f'{nova_frase} é Palidromo')

else:
    print(f'{nova_frase} não é um Palindromo')

