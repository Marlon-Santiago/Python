num = int(input('Digite um número : '))

primo = 0

for c in range(1, num+1):
    if num % c == 0:
        primo += 1

if primo == 2:
    print(f'O numero {num} foi dividido {primo} vezes por isso ele é primo')

else:
    print(f'O numero {num} foi dividido {primo} vezes por isso ele não é primo')
        
