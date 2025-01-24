from datetime import date

anoatual = date.today().year

ano = int(input('Digite o ano de nascimento: '))

idade = anoatual - ano

if idade <= 9:
    print('A categoria do atleta é MIRIM')

elif idade > 9 and idade <= 14:
    print('A categoria desse atleta é INFANTIL')

elif idade > 14 and idade <= 19:
    print('A categoria do atleta é JUNIOR')

elif idade > 19 and idade <= 25:
    print('A categoria do atleta é SÉNIOR')

else:
    idade > 25
    print('Atelta de categotia MASTER')