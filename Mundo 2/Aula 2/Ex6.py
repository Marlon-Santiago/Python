termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

print(termo)

for i in range(0,9):
    termo += razao
    print(termo, end = ' -> ') 

print('acabou')



