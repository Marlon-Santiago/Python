'''
INTERPOLAÇÃO BASICA DE STRINGS COM %

s --> string

d e i --> int

f --> float

x e X --> Hexadecimal (ABCDEF0123456789) 

'''

nome  = 'Marlon'
preco = 1000.145236

variavel = '%s, O preço é %.2f' % (nome, preco)
print(variavel)
